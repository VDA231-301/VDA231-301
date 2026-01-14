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

### Dateinamen
- Der Dateiname des Subschemas:
  - muss die eindeutige Kennung enthalten
  - muss mit `.schema.json` enden.
  - kann zusätzliche Informationen wie das Jahr der Norm enthalten (z.B. EN 10204:2004 -> `VDA_231-301_EN10204_2004_Certificate_3.1.schema.json`).
  - sollte Unterstriche (`_`) anstelle von Leerzeichen verwenden.
  - darf die Versionsnummer nicht im Dateinamen enthalten (nur die Dateien im Delivery-Repository enthalten die Version).
  - Beispiel: `VDA_231-301_VDA278_Thermodesorption.schema.json`

- Der Dateiname der Beispiel-JSON-Datei:
  - muss denselben Basis-Dateinamen wie das zugehörige Subschema haben
  - muss mit `.example.json` enden, um anzuzeigen, dass es sich um eine Beispieldatei handelt.
  - Beispiel: `VDA_231-301_VDA278_Thermodesorption.example.json`

### $id-Eigenschaft

Wichtig: Die $id-Eigenschaft muss das folgende Format haben:

`https://vda231-301.github.io/schemas/{NAME}/VDA_231-301_{NAME}[_ZUSATZ_INFO]_v{VERSION}.schema.json`

wobei:
- `{NAME}` die eindeutige Kennung des Subschemas ist (z.B. `VDA278`, `EN10204`).
- `[_ZUSATZ_INFO]` optional ist und weitere Details wie das Jahr der Norm oder bestimmte Prüfserien enthalten kann.
- `{VERSION}` die Versionsnummer des Subschemas ist.

Dies ist wichtig, um sicherzustellen, dass jedes Subschema eindeutig identifiziert und aufgerufen werden kann.
Freigegebene Versionen aller Schemata werden im [Schemas-Repository](https://github.com/VDA231-301/schemas) gespeichert und sind immer unter derselben URL zugänglich.

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

## 5. Technische Umsetzung

### Referenz auf das generische Schema
Subschemata müssen die Version des generischen Schemas, auf dem sie basieren, mittels JSON-Zeigern (`$ref`) referenzieren.
Die Wurzel des Subschemas muss `allOf` verwenden, um das Basisschema einzubinden, und kann dann zusätzliche Eigenschaften oder Einschränkungen definieren.

Beispiel:

```json
{
  "$id": "https://vda231-301.github.io/schemas/VDA_278/VDA_231-301_VDA_278_v0.1.0.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "VDA 231-301 TestReport JSON schema for VDA 278",
  "allOf": [
    {
      "$ref": "https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v0.2.0.schema.json"
    }
  ],
  "type": "object",
  "properties": {
    ...
  }
}
```

### Bedingte Logik für die Anwendbarkeit des Subschemas

Ziel: Das Subschema sollte nur gelten, wenn der Prüfbericht Daten für die spezifische Norm enthält. Das bedeutet, wenn eine Prüfbericht-JSON erfolgreich gegen das Subschema validiert wird, enthält sie Daten für die angegebene Norm.

Subschemata validieren das Vorhandensein erforderlicher Prüfdaten durch Prüfung des `TestSeries`-Arrays. Es gibt zwei primäre Ansätze für diese Validierung:

#### Ansatz 1: Abgleich über TestType

Wenn die Norm bestimmte Prüfarten definiert, verwenden Sie die `TestType`-Eigenschaft, um relevante Prüfserien zu identifizieren:
```json
{
  "allOf": [
    {
      "$ref": "https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v0.2.0.schema.json"
    },
    {
      "properties": {
        "TestSeries": {
          "type": "array",
          "contains": {
            "type": "object",
            "properties": {
              "TestType": {
                "const": "Thermodesorption"
              }
            },
            "required": ["TestType"]
          }
        }
      }
    }
  ]
}
```

Für Normen, die mehrere Prüfarten erfordern (z.B. EN 10204, die sowohl chemische Zusammensetzung als auch Zugversuch erfordert), verwenden Sie `allOf` mit mehreren `contains`:
```json
{
  "properties": {
    "TestSeries": {
      "type": "array",
      "allOf": [
        {
          "contains": {
            "type": "object",
            "properties": {
              "TestType": {
                "const": "Optical Emission Spectroscopy"
              }
            },
            "required": ["TestType"]
          }
        },
        {
          "contains": {
            "type": "object",
            "properties": {
              "TestType": {
                "const": "Tensile testing"
              }
            },
            "required": ["TestType"]
          }
        }
      ]
    }
  }
}
```

#### Ansatz 2: Abgleich über Specification

Wenn Prüfserien durch die Norm-Spezifikation selbst identifiziert werden, führen Sie den Abgleich gegen das `Specification`-Objekt durch:
```json
{
  "properties": {
    "TestSeries": {
      "type": "array",
      "contains": {
        "type": "object",
        "properties": {
          "Specification": {
            "type": "object",
            "properties": {
              "Authority": { "const": "VDA" },
              "Number": { "const": "278" }
            },
            "required": ["Authority", "Number"]
          }
        },
        "required": ["Specification"]
      }
    }
  }
}
```

#### Ansatz 3: Abgleich über TestType UND Specification

Für eine strengere Validierung können sowohl TestType- als auch Specification-Eigenschaften gleichzeitig abgeglichen werden:
```json
{
  "properties": {
    "TestSeries": {
      "type": "array",
      "contains": {
        "type": "object",
        "properties": {
          "TestType": { "const": "Thermodesorption" },
          "Specification": {
            "type": "object",
            "properties": {
              "Authority": { "const": "VDA" },
              "Number": { "const": "278" }
            },
            "required": ["Authority", "Number"]
          }
        },
        "required": ["TestType", "Specification"]
      }
    }
  }
}
```

Dieser Ansatz gewährleistet maximale Konsistenz, indem sowohl die Prüfart als auch die Norm-Spezifikation explizit definiert und mit den erwarteten Werten abgeglichen werden müssen.


#### Wichtige Hinweise:
- Die `required`-Eigenschaft ist in jedem `contains`-Block unerlässlich, um sicherzustellen, dass die übereinstimmenden Objekte tatsächlich die angegebenen Eigenschaften haben
- Das Schlüsselwort `contains` stellt sicher, dass mindestens ein Array-Element den Kriterien entspricht
- Die Verwendung von `allOf` mit mehreren `contains` erfordert, dass alle angegebenen Prüfarten vorhanden sind
- Subschemata können diese Bedingungen mit zusätzlichen Eigenschaftsbeschränkungen kombinieren, indem sie `$ref` verwenden, um detaillierte Prüfserien-Definitionen zu referenzieren

---

## 6. KI-gestützte Erstellung von Subschemata
KI-Tools können zur Unterstützung bei der Erstellung von Subschemata verwendet werden. Sie können helfen bei:
- Erstellung von ersten Entwürfen basierend auf der Dokumentation der Norm.
- Vorschlägen für Eigenschaftsnamen und Strukturen.
- Erstellung von Beispiel-JSON-Dateien.

Es ist jedoch entscheidend, dass menschliche Aufsicht gewährleistet ist, um Genauigkeit, Einhaltung der Richtlinien und korrekte Repräsentation der Norm sicherzustellen.

### Beispiel-Prompt für KI-Tools:
```
There is a project based on JSON schema that aims to provide a standard way for digital test results to be represented and exchanged.
Here's the link to the project:
https://raw.githubusercontent.com/VDA231-301/VDA231-301/refs/heads/main/README.md
Look especially at this guide: https://raw.githubusercontent.com/VDA231-301/VDA231-301/refs/heads/main/docs/guidelines_for_creating_subschemas_VDA231-301_en.md
And this specific sub-schema:
https://vda231-301.github.io/schemas/EN_10204/VDA_231-301_EN_10204_2004_Certificate_3.1_v0.2.0.schema.json
Now I want you to create a new sub-schema for the standard "<Insert name / title of you standard here>".
I will upload the PDF document for this standard.
I will also provide a sample test report PDF document based on the standard to help you create the sub-schema and example files.
Please make sure the sub-schema follows the guidelines provided in the link above and captures all relevant information from the <Insert name of your standard here> standard.
Create a JSON schema document and an example JSON test report file based on the new sub-schema.
The example must validate against the created sub-schema, which also means it must validate against the generic VDA 231-301 schema found here: https://vda231-301.github.io/schemas/generic/VDA_231-301_generic_v0.2.0.schema.json (This requirement is crucial and listed in the guidelines, it must be achieved via "allOf" referencing the generic schema).
```

> **Hinweis:** Wenn Sie diesen Prompt verwenden, ersetzen Sie bitte `<Insert name / title of you standard here>` und `<Insert name of your standard here>` durch den tatsächlichen Namen der Norm, an der Sie arbeiten, und fügen Sie zwei PDF-Dokumente bei: eines für die Norm und eines für einen Beispiel-Prüfbericht basierend auf dieser Norm.

## 7. Veröffentlichung und Review

- Neue Subschemata können jederzeit der Projektgruppe (PG) im VDA vorgeschlagen werden.
- Der Einreichungsprozess ist im Repository dokumentiert: [Prozessablaufdiagramm](./assets/process%20flows/process_flow_release_of_new_specialised_schemas_EN.svg)
- Nach erfolgreicher Prüfung durch die PG erfolgt die Veröffentlichung.

---

> **Tipp:** Schau dir die bestehenden Beispiele und das generische Basisschema im GitHub-Repository an, um die Struktur und Konventionen zu übernehmen.



---