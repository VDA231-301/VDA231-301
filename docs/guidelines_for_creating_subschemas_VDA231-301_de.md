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