"""Validate the clamp JSON and its references; does not validate binary JT geometry."""
import json
import re
import sys
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

HERE = Path(__file__).resolve().parent
SCHEMA = HERE.parents[1] / "main/VDA_231-301_Schema_Generic.json"
EXAMPLE = HERE / "VDA_231-301_ToggleClamp_SubComponents.example.json"


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def validate():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data))
    check(not errors, "\n".join(f"{list(e.absolute_path)}: {e.message}" for e in errors))
    nodes = list(objects(data))
    identified = [n for n in nodes if "_id" in n]
    ids = {n["_id"]: n for n in identified}
    check(len(ids) == len(identified), "Duplicate _id")
    for identifier in ids:
        parsed = uuid.UUID(identifier)
        check(parsed.version == 4 and str(parsed) == identifier, f"Invalid UUID v4: {identifier}")
    reference_types = {
        "ContractorID": "TestingCenter", "TestingCenterID": "TestingCenter",
        "ComponentMasterID": "ComponentMaster", "AlsoApplicableComponentMasterIDs": "ComponentMaster",
        "ComponentInstanceID": "ComponentInstance", "SpecimenID": "Specimen",
        "PredecessorID": "TestSeries", "SuccessorID": "TestSeries",
    }
    references = 0
    for node in nodes:
        for key, expected_type in reference_types.items():
            value = node.get(key)
            for ref in value if isinstance(value, list) else ([] if value is None else [value]):
                check(ref in ids and ids[ref]["_type"] == expected_type, f"Invalid {key}: {ref}")
                references += 1
    masters = [n for n in nodes if n.get("_type") == "ComponentMaster"]
    instance_owners = {i["_id"]: m["_id"] for m in masters for i in m.get("Instances", [])}
    for topic in data["Topics"]:
        specimens = {s["_id"]: s for s in topic["Specimens"]}
        check(topic["NumberOfExecutions"] == len(topic["Executions"]), "Execution count mismatch")
        check(topic["ComponentMasterID"] not in topic.get("AlsoApplicableComponentMasterIDs", []),
              "Primary component repeated in AlsoApplicableComponentMasterIDs")
        for execution in topic["Executions"]:
            check(execution["SpecimenID"] in specimens, "Specimen must belong to the containing topic")
            specimen = specimens[execution["SpecimenID"]]
            check(instance_owners[specimen["ComponentInstanceID"]] == topic["ComponentMasterID"],
                  "Specimen instance belongs to another component")
        for key, inverse in [("PredecessorID", "SuccessorID"), ("SuccessorID", "PredecessorID")]:
            if topic.get(key):
                check(ids[topic[key]].get(inverse) == topic["_id"], "Non-reciprocal topic link")
    for node in nodes:
        if "ArraySpec" in node and "ArrayValue" in node:
            check(all(len(row) == len(node["ArraySpec"]) for row in node["ArrayValue"]),
                  "ArrayValue row width differs from ArraySpec")

    # Read assembly occurrence chains from the supplied ASCII JT export.
    ajt = (HERE / "Toggle_Clamp__VDA+all_CAD_.ajt").read_text(encoding="latin1")
    chains, stack, depth = set(), [], 0
    for line in ajt.splitlines():
        assembly = re.match(r"(\d+)\s+ASM\s", line)
        if assembly:
            depth = int(assembly[1])
            stack = stack[:max(0, depth - 1)]
        uid = re.search(r'Key="__CAD_INST_UID"\s+Value="([^"]+)"', line)
        if uid:
            check(depth == len(stack) + 1, "Unexpected ASCII JT assembly depth")
            stack.append(uid[1])
            chains.add(tuple(stack))

    # Inspect bounded Part text blocks for source-token matching.
    # XML syntax is checked separately below; neither check validates JT conformance.
    xml_path = HERE / "Toggle_Clamp__VDA+all_CAD_.xml"
    xml_text = xml_path.read_text(encoding="latin1")
    parts = {}
    for match in re.finditer(r'<Part\b([^>]+)>(.*?)</Part>', xml_text, re.S):
        attrs = dict(re.findall(r'(\w+)="([^"]*)"', match[1]))
        token = f'{attrs["name"]}.part;{attrs["version"]};{attrs["id"]}:'
        properties = {key: value.strip('"') for key, value in re.findall(
            r'<Property[^>]*key="([^"]+)"[^>]*><!\[CDATA\[(.*?)\]\]></Property>', match[2], re.S)}
        parts[token] = properties
    paths = []
    for master in masters:
        path = master.get("NGIDPath")
        if not path:
            continue
        paths.append(path)
        prefix = '$$NGID<chain>="__CAD_INST_UID"\\0'
        check(path.startswith(prefix) and path.endswith('\\0\\0'), "Unexpected NGID syntax")
        segments = path[len(prefix):-4].split('\\0')
        body = segments.pop() if '.part;' in segments[-1] else None
        check(tuple(segments) in chains, f"Assembly chain missing from ASCII JT: {path}")
        if body:
            check(body in parts, f"Part token missing from XML text: {body}")
            source = parts[body]
            check(master["MaterialClass"] == source["MAT_06_SHORT_NAME::"], "Material class differs from CAD")
            check(master["MaterialIdentifiers"] == [
                {"IdentifierType": "OEMMATID", "Value": source["MAT_01_SPECIFICATION_IDENTIFIER::"]}
            ], "Material identifier differs from CAD")
    check(len(paths) == len(set(paths)), "Duplicate NGID occurrence path")
    print(f"PASS: schema; {len(ids)} unique UUIDs; {references} typed references; topic/specimen consistency")
    print(f"PASS: {len(masters)} component masters; {len(paths)} unique NGID paths; CAD assembly chains and material tokens")
    print("LIMIT: body tokens are matched by name/version/id, not resolved through a JT viewer.")
    try:
        ET.parse(xml_path)
    except ET.ParseError as error:
        print(f"WARNING: XML is not well-formed: {error}")
    else:
        print("PASS: XML is well-formed; JT conformance and NGID resolution remain unverified.")
    print("LIMIT: source revisions, material-key uniqueness, specification content and engineering results are not certified.")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, KeyError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
