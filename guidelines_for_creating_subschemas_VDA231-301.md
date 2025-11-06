# Instructions: Subschema Creation according to VDA 231-301 (English)

## 1. Purpose and Goal of a Subschema

A subschema serves to precisely define the contents of a specification and to further restrict the general format of the base schema. This ensures that test results for a specific specification can always be exchanged in the same format. The subschema defines:

- Which attribute-value pairs are permitted (nomenclature of the specification)
- Which attributes must be included
- That compatibility with the base schema is maintained. Successful validation against a subschema means that the testing project contains data for the specified specification. Documents should still always be validated against the base schema to ensure overall compliance.

---

## 2. Procedure for Subschema Creation

- **Standard Data Modeling:** Follow best practices, but a compromise must be found between practicality and level of detail.
- **Units:** SI or metric units are recommended, but not mandatory.
- **Tables:** Are mapped as arrays. If arrays are to be validated, the table definition (columns/rows) must be done exactly in the subschema. If a precise definition of the properties is required, e.g., a carbon content must always be specified, the results (`SingleResults` & `ConsolidatedCharacteristicValues`) should not be modeled as `InformationSet`, but in the stricter form `SingleResultPoint` or `CharacteristicValuePoint`.
- **Technical properties:** The `_id` and `_type` properties should be included in subschemas for all objects that also have them in the base schema. Subschemas can add relations using pointers to an entities' `_id` property like for example the `ComponentInstanceID` in the base schema.

---

## 3. Naming and Prefixing
### Naming
- Each subschema receives a unique identifier, usually related to the standard, e.g., "
VDA278" for results of thermodesorption or "EN10204" for 3.1 test certificates.
- This identifier is used in the file name and URL structure to uniquely identify the subschema.

### Prefixing
- Additionally, each subschema can use prefixes in the definitions in the JSON schema file to avoid naming conflicts or to clarify affiliation.
- Example:
  - In the schema `VDA278`:
  ```json
  {
    "VDA278.ProcessDataPreconditioningEndDate": {
      "type": "object",
      "properties": {
        "Property": {
          "const": "End date"
        },
        "Value": {
          "$ref": "#/$defs/Generic.Date"
        }
      }
    }
  }
  ```
  - In the schema `EN10204`, different prefixes are used to distinguish the individual test series (tensile test and chemical composition):
  ```json
  {
   "3-1_Certificate.ChangeOfWidth": {
      "properties": {
        "Property": {
          "const": "Change of Width"
        },
        "Unit": {
          "const": "mm"
        }
      },
      "required": [
        "Property",
        "Unit"
      ],
      "type": "object"
    },
     "3-1_Composition_Certificate.SubstanceCAS": {
      "properties": {
        "Property": {
          "const": "Substance CAS"
        }
      },
      "required": [
        "Property"
      ],
      "type": "object"
    },
    "3-1_Tensile_Certificate.TestSeries": {
      ...
    }
  }
  ```
---

## 4. Conditional Logic

> TODO MP
- Conditions can be based on specific values or the presence of attributes in the main schema.
- The logic is mapped with the keywords `if`, `then`, `else` in the schema.

---

## 5. Technical Implementation

Subschemas are versioned and hosted on GitHub:  
https://github.com/VDA231-301/schemas

References to other schemas are made via JSON pointers (`$ref`).

### Example for naming a subschema

Important: The $id property must follow the format:

`https://vda231-301.github.io/schemas/{NAME}/VDA_231-301_{NAME}_v{VERSION}.schema.json`

```json
{
  "$id": "https://vda231-301.github.io/schemas/VDA_278/VDA_231-301_VDA_278_v0.1.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for VDA 278"
}
```

```json
{
  "$id": "https://vda231-301.github.io/schemas/EN_10204/VDA_231-301_EN_10204_2004_Certificate_3.1_v0.2.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for EN_10204_2004_Certificate_3.1"
}
```

---

## 6. Publication and Review

- New subschemas can be proposed to the project group (PG) in the VDA at any time.
- The submission process is documented in the repository.
- Publication takes place after successful review by the PG.

---

> **Tip:** Take a look at the existing examples and the generic base schema in the GitHub repository to adopt the structure and conventions.

---

# Anleitung: Subschema-Erstellung nach VDA 231-301 (Deutsch)

## 1. Ziel und Zweck eines Subschemas

Ein Subschema dient dazu, die Inhalte einer Spezifikation präzise zu definieren und das allgemeine Format des Basisschemas weiter einzuschränken. Dadurch wird sichergestellt, dass Prüfergebnisse für eine bestimmte Spezifikation immer im gleichen Format ausgetauscht werden können. Das Subschema legt fest:

- Welche Attribut-Werte-Paare zulässig sind (Nomenklatur der Spezifikation)
- Welche Attribute zwingend enthalten sein müssen
- Dass die Kompatibilität zum Basisschema erhalten bleibt. Eine erfolgreiche Validierung gegen ein Subschema bedeutet, dass das Prüfprojekt Daten für die angegebene Spezifikation enthält. Dokumente sollten dennoch stets auch gegen das Basisschema validiert werden, um die Gesamtkonformität sicherzustellen.

---

## 2. Vorgehen bei der Subschema-Erstellung

- **Standard-Datenmodellierung:** Folge Best Practices, aber es gilt einen Kompromiss zwischen Praxisnähe und Detailtiefe zu finden.
- **Einheiten:** SI- oder metrische Einheiten werden empfohlen, sind aber nicht zwingend vorgeschrieben.
- **Tabellen:** Werden als Arrays abgebildet. Sollen Arrays validiert werden, muss die Tabellendefinition (Spalten/Zeilen) im Subschema exakt erfolgen. Wenn eine genaue Definition der Eigenschaften erforderlich ist, z.B. ein Kohlenstoffgehalt muss immer angegeben werden, sollten die Ergebnisse (`SingleResults` & `ConsolidatedCharacteristicValues`) nicht als `InformationSet`, sondern in der strikteren Form `SingleResultPoint` bzw. `CharacteristicValuePoint` modelliert werden.
- **Technische Eigenschaften:** Die Eigenschaften `_id` und `_type` sollten in Subschemata für alle Objekte enthalten sein, die diese auch im Basisschema besitzen. Subschemata können Beziehungen mittels Zeigern auf die `_id`-Eigenschaft von Entitäten hinzufügen, wie zum Beispiel die `ComponentInstanceID` im Basisschema.

---

## 3. Namenskennung und Präfixierung

### Namenskennung
- Jedes Subschema erhält ein eindeutige Kennung, in der Regel auf die Norm bezogen, z.B. "VDA278" für Ergebnisse der Thermodesorption oder "EN10204" für 3.1 Prüfzeugnisse.
- Diese Kennung wird im Dateinamen und in der URL Struktur verwendet, um das Subschema eindeutig zu identifizieren.

### Präfixierung
- Zusätzlich kann jedes Subschema in den Definitionen im JSON Schema File Präfixe verwenden, um Namenskonflikte zu vermeiden bzw. die Zugehörigkeit zu verdeutlichen.
- Beispiel:
  - Im Schema `VDA278`:
  ```json
  {
    "VDA278.ProcessDataPreconditioningEndDate": {
      "type": "object",
      "properties": {
        "Property": {
          "const": "End date"
        },
        "Value": {
          "$ref": "#/$defs/Generic.Date"
        }
      }
    }
  }
  ```
  - Im Schema `EN10204` werden unterschiedliche Präfixe verwendet um die einzelnen Prüfserien (Zugversuch und chemische Zusammensetzung) zu unterscheiden:
  ```json
  {
   "3-1_Certificate.ChangeOfWidth": {
      "properties": {
        "Property": {
          "const": "Change of Width"
        },
        "Unit": {
          "const": "mm"
        }
      },
      "required": [
        "Property",
        "Unit"
      ],
      "type": "object"
    },
     "3-1_Composition_Certificate.SubstanceCAS": {
      "properties": {
        "Property": {
          "const": "Substance CAS"
        }
      },
      "required": [
        "Property"
      ],
      "type": "object"
    },
    "3-1_Tensile_Certificate.TestSeries": {
      ...
    }
  }
  ```

---

## 4. Bedingte Logik

> TODO MP
- Bedingungen können auf bestimmte Werte oder das Vorhandensein von Attributen im Hauptschema basieren.
- Die Logik wird mit den Schlüsselwörtern `if`, `then`, `else` im Schema abgebildet.

---

## 5. Technische Umsetzung

Freigegebene Subschemata werden auf GitHub versioniert und gehostet:  
https://vda231-301.github.io/schemas/

Referenzen auf andere Schemata erfolgen über JSON-Zeiger (`$ref`).

Die freigegebenen Versionen des Basisschemas finden sich im Verzeichnis "generic":
https://vda231-301.github.io/schemas/generic

### Beispiel für die Benennung eines Subschemas

Wichtig: Die $id Eigenschaft muss das folgende Format haben:

`https://vda231-301.github.io/schemas/{KENNUNG}/VDA_231-301_{KENNUNG}_v{VERSION}.schema.json`

```json
{
  "$id": "https://vda231-301.github.io/schemas/VDA_278/VDA_231-301_VDA_278_v0.1.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for VDA 278"
}
```

```json
{
  "$id": "https://vda231-301.github.io/schemas/EN_10204/VDA_231-301_EN_10204_2004_Certificate_3.1_v0.2.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for EN_10204_2004_Certificate_3.1"
}
```

---

## 6. Veröffentlichung und Review

- Neue Subschemata können jederzeit der Projektgruppe (PG) im VDA vorgeschlagen werden.
- Der Prozess zur Einreichung ist im Repository dokumentiert.
- Nach erfolgreicher Prüfung durch die PG erfolgt die Veröffentlichung.

---

> **Tipp:** Schau dir die bestehenden Beispiele und das generische Basisschema im GitHub-Repository an, um die Struktur und Konventionen zu übernehmen.



---