# Parsing-Regeln für Norm-Strings (VDA 231-300 → 231-301)

**Zweck:** Zerlegung eines kombinierten Norm-/Liefervorschrift-Strings (wie er in der
CAD-Werkstoffliste bzw. der Oberflächendatenbank als **ein** Feld vorliegt) in die getrennten
VDA-231-300-Attribute `REGULATION_TYPE` (MAT_02/SUR_02), `REGULATION_NUMBER` (MAT_03/SUR_03) und
– abgeleitet – `LEGAL_AUTHORITY` (MAT_04/SUR_04). Ziel-Entität im 231-301: eingebettete
`Specification` (`Type`, `Number`, `SubNumber`, `Authority`).

> **Casing-Konvention:** Das Subnummern-Feld heißt durchgängig **`SubNumber`** (großes N),
> konsistent mit der getroffenen Casing-Entscheidung.

> **Anonymisierung:** Öffentliche Normprefixe (DIN, EN, DIN EN, ISO, VDA) bleiben real, da es
> allgemeine Kategorien sind. OEM-interne Prefixe sind neutralisiert:
> `OEMSPEC` = interne Liefervorschrift (statt der realen OEM-Abkürzung),
> `OEMSTD` = interne Werknorm. Alle Nummern und Schlüssel sind fiktiv.

---

## 1. Grundmuster eines Norm-Strings

```
[ TYPE ] [ optionales Leerzeichen ] NUMBER [ Trenner SUBNUMBER ]
   │                                   │        │
   │                                   │        └── "." (interne Ausführungsart/Stand)  oder
   │                                   │            "-" (Teil einer DIN/EN-Norm)
   │                                   └── Kernnummer (Ziffern)
   └── ein oder mehrere Präfix-Token (z. B. "DIN", "EN", "DIN EN", "ISO", "OEMSPEC", "OEMSTD")
```

Beobachtete Varianten in den Quelldaten:
- **mit** Leerzeichen: `DIN EN 10267`, `OEMSPEC 5105.00`
- **ohne** Leerzeichen: `OEMSPEC5029.00`  (kommt in den „Weitere Norm"-Spalten vor)
- **Teilnummer mit Bindestrich**: `DIN EN 10263-4`, `EN 10277-3`
- **Ausführungsart/Stand mit Punkt**: `OEMSPEC 9385.20`, `OEMSPEC 5105.00`

---

## 2. Verarbeitungsschritte (Pipeline)

1. **Normalisieren**
   - `trim()`, Mehrfach-Leerzeichen auf eines reduzieren.
   - Fehlendes Leerzeichen zwischen Alpha-Präfix und erster Ziffer einfügen
     (`OEMSPEC5029.00` → `OEMSPEC 5029.00`).
2. **TYPE erkennen (greedy, längste Übereinstimmung zuerst)**
   - Bekannte Präfixe aus kontrollierter Liste matchen; **mehrwortige zuerst**
     (`DIN EN` **vor** `DIN`, sonst wird `EN` fälschlich zur Nummer).
3. **NUMBER/SUBNUMBER trennen**
   - Rest nach TYPE = Nummernteil.
   - Enthält Nummernteil `.` → alles nach dem letzten sinnvollen Punkt = `SubNumber`
     (interne Ausführungsart/Stand). Beispiel: `5105.00` → Number `5105`, SubNumber `00`.
   - Enthält Nummernteil `-` (DIN/EN-Familie) → Teil-Nummer = `SubNumber`.
     Beispiel: `10263-4` → Number `10263`, SubNumber `4`.
4. **AUTHORITY ableiten** (Lookup, siehe Abschnitt 4).
5. **Validieren** (Abschnitt 5) und Restfehler in `_parseWarnings` protokollieren.

---

## 3. Regex (Referenz)

```regex
# Normalisierung: Leerzeichen zwischen Präfix und Ziffer erzwingen
NORMALIZE_INSERT_SPACE = /^([A-Za-zÄÖÜ ]+?)(\d)/   → "$1 $2"

# Haupt-Zerlegung (nach Normalisierung)
NORM_STRING = /^(?<type>DIN EN|DIN|EN|ISO|VDA|OEMSPEC|OEMSTD)\s+(?<num>\d+)(?:(?<sep>[.\-])(?<sub>[0-9A-Za-z]+))?\s*$/
```

- `type` : kontrollierte Präfixliste (erweiterbar).
- `num`  : Kernnummer (Ziffern).
- `sep`  : Trenner – `.` → interne Ausführungsart/Stand, `-` → Teil (DIN/EN).
- `sub`  : SubNumber (optional).

---

## 4. Herausgeber-Mapping (TYPE → AUTHORITY, MAT_04/SUR_04)

| TYPE (Präfix) | AUTHORITY (Herausgeber) | Anmerkung |
|---|---|---|
| `DIN` | DIN e.V. | nationale Norm |
| `EN` | CEN (dt. Ausgabe via DIN) | europäische Norm |
| `DIN EN` | DIN e.V. / CEN | harmonisierte EN als DIN-Ausgabe |
| `ISO` | ISO | internationale Norm |
| `VDA` | VDA | Verband der Automobilindustrie |
| `OEMSPEC` | *OEM (anonymisiert)* | interne Liefervorschrift |
| `OEMSTD` | *OEM (anonymisiert)* | interne Werknorm |

> Das Mapping ist eine **ANNAHME** und als konfigurierbare Lookup-Tabelle zu pflegen.
> `IssueDate` (MAT_05/SUR_05) ist **nicht** aus dem String ableitbar → aus der Normenverwaltung
> ergänzen; im ERM ist `Specification.IssueDate` vorhanden.

---

## 5. Validierungsregeln

- **TYPE** muss in der kontrollierten Liste enthalten sein; sonst `WARNING: unknown regulation type`.
- **NUMBER** darf nicht leer sein; VDA 231-300: alphanum. max. 16 Zeichen.
- **SUBNUMBER-Konvention**:
  - Punkt (`.`) → interne Ausführungsart/Stand (typisch bei `OEMSPEC`).
  - Bindestrich (`-`) → Teil einer DIN/EN-Norm.
- Bei mehr als einem Trenner → nur erster als SubNumber, Rest in `_parseWarnings`.

---

## 6. Worked Examples (anonymisiert)

### 6.1 Material (Quelle: CAD-Werkstoffliste, Spalte „Werkstoffnorm/Liefervorschrift")

| Eingabe-String | → Type | → Number | → SubNumber | → Authority (abgeleitet) |
|---|---|---|---|---|
| `DIN EN 10267` | DIN EN | 10267 | – | DIN e.V. / CEN |
| `DIN EN 10263-4` | DIN EN | 10263 | 4 | DIN e.V. / CEN |
| `EN 10277-3` | EN | 10277 | 3 | CEN |
| `OEMSPEC 5105.00` | OEMSPEC | 5105 | 00 | OEM (anonym.) |
| `OEMSPEC5029.00` *(kein Space)* | OEMSPEC | 5029 | 00 | OEM (anonym.) |

### 6.2 Oberfläche (Quelle: MBN-Oberflächendatenbank, Feld „Beschichtungs-/Oberflächennorm")

| Eingabe-String | → Type | → Number | → SubNumber | → Authority (abgeleitet) |
|---|---|---|---|---|
| `OEMSPEC 2652` | OEMSPEC | 2652 | – | OEM (anonym.) |
| `OEMSPEC 9385.20` | OEMSPEC | 9385 | 20 | OEM (anonym.) |
| `OEMSTD 90550` | OEMSTD | 90550 | – | OEM (anonym.) |

### 6.3 Beispielausgabe als `Specification`-Fragment (JSON)

```json
{
  "Type": "DIN EN",
  "Number": "10263",
  "SubNumber": "4",
  "Authority": "DIN e.V. / CEN",
  "IssueDate": null
}
```

---

## 7. Referenz-Implementierung (Python, drop-in für den Konverter)

```python
import re

KNOWN_TYPES = ["DIN EN", "DIN", "EN", "ISO", "VDA", "OEMSPEC", "OEMSTD"]  # längste zuerst!
AUTHORITY = {
    "DIN": "DIN e.V.", "EN": "CEN", "DIN EN": "DIN e.V. / CEN",
    "ISO": "ISO", "VDA": "VDA", "OEMSPEC": "OEM", "OEMSTD": "OEM",
}

def parse_norm_string(raw: str) -> dict:
    warnings = []
    s = re.sub(r"\s+", " ", (raw or "").strip())
    s = re.sub(r"^([A-Za-zÄÖÜ ]+?)(\d)", r"\1 \2", s)  # fehlendes Leerzeichen einfügen
    s = re.sub(r"\s+", " ", s).strip()

    rtype = next((t for t in KNOWN_TYPES if s.upper().startswith(t.upper() + " ")), None)
    if rtype is None:
        return {"Type": None, "Number": None, "SubNumber": None,
                "Authority": None, "_parseWarnings": ["unknown regulation type"], "_raw": raw}

    rest = s[len(rtype):].strip()
    m = re.match(r"^(\d+)(?:([.\-])([0-9A-Za-z]+))?(.*)$", rest)
    if not m:
        return {"Type": rtype, "Number": None, "SubNumber": None,
                "Authority": AUTHORITY.get(rtype), "_parseWarnings": ["no number found"], "_raw": raw}

    number, sep, sub, tail = m.group(1), m.group(2), m.group(3), m.group(4).strip()
    if tail:
        warnings.append(f"unparsed tail: '{tail}'")
    return {
        "Type": rtype,
        "Number": number,
        "SubNumber": sub,                 # '.' = interne Ausführungsart/Stand, '-' = Teil (DIN/EN)
        "Authority": AUTHORITY.get(rtype),
        "IssueDate": None,                # aus Normenverwaltung ergänzen (MAT_05/SUR_05)
        "_parseWarnings": warnings or None,
    }

# --- Testfälle (anonymisiert) ---
if __name__ == "__main__":
    for s in ["DIN EN 10267", "DIN EN 10263-4", "EN 10277-3",
              "OEMSPEC 5105.00", "OEMSPEC5029.00", "OEMSPEC 9385.20", "OEMSTD 90550"]:
        print(f"{s:20} -> {parse_norm_string(s)}")
```

Getestete Ausgabe (verifiziert):

```
DIN EN 10267       -> Type=DIN EN, Number=10267, SubNumber=None,  Authority=DIN e.V. / CEN
DIN EN 10263-4     -> Type=DIN EN, Number=10263, SubNumber=4,     Authority=DIN e.V. / CEN
EN 10277-3         -> Type=EN,     Number=10277, SubNumber=3,     Authority=CEN
OEMSPEC 5105.00    -> Type=OEMSPEC, Number=5105, SubNumber=00,    Authority=OEM
OEMSPEC5029.00     -> Type=OEMSPEC, Number=5029, SubNumber=00,    Authority=OEM
OEMSPEC 9385.20    -> Type=OEMSPEC, Number=9385, SubNumber=20,    Authority=OEM
OEMSTD 90550       -> Type=OEMSTD, Number=90550, SubNumber=None,  Authority=OEM
```

---

## 8. Hinweise / offene Punkte

- **`.` vs. `-`**: Die Konvention (Punkt = interne Ausführungsart/Stand, Bindestrich = DIN/EN-Teil)
  ist als **ADR** festzuhalten, damit die Zuordnung reproduzierbar ist.
- **Kontrollierte Präfixliste** und **Authority-Mapping** müssen gepflegt werden (neue Prefixe).
- **`Authority`** (MAT_04/SUR_04) wird aus `Type` abgeleitet (ADR 0006); **`IssueDate`**
  (MAT_05/SUR_05) ist im ERM als `Specification.IssueDate` vorhanden und aus der Normenverwaltung
  zu befüllen.
- Alle OEM-internen Bezeichnungen in diesem Dokument sind **anonymisiert** (`OEMSPEC`/`OEMSTD`).
- Casing: durchgängig **`SubNumber`** (großes N).
