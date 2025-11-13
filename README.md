# Factory Business Simulation - Dokumentation
## Planspiel BWL für BDE - WiSe 2025/26

**Ostfalia Hochschule für angewandte Wissenschaften**  
**Fakultät Maschinenbau**  
**Institut für Produktionstechnik**

---

## 📋 Inhaltsverzeichnis

1. [Projektübersicht](#projektübersicht)
2. [Anforderungen und Ziele](#anforderungen-und-ziele)
3. [Implementierte Funktionen](#implementierte-funktionen)
4. [Technische Architektur](#technische-architektur)
5. [Benutzungsanleitung](#benutzungsanleitung)
6. [Formeln und Berechnungen](#formeln-und-berechnungen)
7. [Installation und Ausführung](#installation-und-ausführung)
8. [Beispielszenarien](#beispielszenarien)

---

## 1. Projektübersicht

Dieses Projekt erweitert das bestehende Factory-Planspiel um variable Parameter und interaktive Elemente, um ein realistischeres und lehrreicheres Wirtschaftssimulationsspiel zu schaffen.

### Entwickelt von
- **Projektname**: Factory Business Simulation - Enhanced Interactive Version
- **Zeitraum**: KW 45 - KW 51 (WiSe 2025/26)
- **Zweck**: Verbesserung des BWL-Planspiels mit variabler Interaktivität

### Hauptmerkmale
- ✅ Variable Verkaufspreise mit Nachfrageelastizität
- ✅ Variabler Marketing-Budget mit Effekt auf Absatz
- ✅ Variable Fertigungskosten (Effizienzfaktoren)
- ✅ Variable Einkaufspreise (Marktfaktoren)
- ✅ Variable Gemeinkosten
- ✅ Prototypische IT-Unterstützung (Python + Web + Excel)

---

## 2. Anforderungen und Ziele

### Ursprüngliche Anforderungen (aus Aufgabenstellung)
Das Projekt sollte das Konzept des Factory-Planspiels so weiterentwickeln, dass:

1. **Der Spielablauf variabler mit mehr Interaktivität gestaltet wird**, mit Optionen für:
   - Variable Verkaufspreise oder Absatzmengen (z.B. nach Marketing-Ausgaben)
   - Variable Fertigungskosten
   - Variable Einkaufspreise
   - Variable Gemeinkosten

2. **Eine geeignete IT-Unterstützung zur Verfolgung/Berechnung konzipiert wird**

3. **Diese prototypisch umgesetzt wird**

### Erreichte Ziele
✅ **Alle Anforderungen vollständig umgesetzt**
- Python-basierter Simulator mit vollständiger Spiellogik
- Web-Interface für einfache Bedienung
- Excel-basierte Alternative für offline Nutzung
- Umfassende Dokumentation

---

## 3. Implementierte Funktionen

### 3.1 Variable Verkaufspreise
- **Preiselastizität der Nachfrage**: Höhere Preise reduzieren die Nachfrage
- **Formel**: `Nachfrage = Basisnachfrage × (1 - (Preisverhältnis - 1) × Elastizität)`
- **Wettbewerbseffekt**: Berücksichtigung von Konkurrenzpreisen

### 3.2 Marketing-Budget
- **Marketing-Effektivität**: Zusätzliche Ausgaben erhöhen die Nachfrage
- **Formel**: `Nachfrageerhöhung = 1 + (Marketing-Budget × Effektivität)`
- **Strategische Entscheidung**: Balance zwischen Kosten und Absatzsteigerung

### 3.3 Variable Produktionskosten
- **Effizienzfaktor**: Produktionsoptimierung reduziert Kosten
- **Qualitätsfaktor**: Qualitätsanforderungen beeinflussen Kosten
- **Formel**: `Kosten = Basiskosten × Effizienzfaktor × Qualitätsfaktor`

### 3.4 Variable Materialpreise
- **Marktfaktoren**: Rohstoffpreisschwankungen
- **Formel**: `Materialkosten = Basispreis × Marktfaktor`
- **Beispiel**: Marktfaktor 1.2 = 20% Preissteigerung

### 3.5 Variable Gemeinkosten
- **Overhead-Faktor**: Anpassung der fixen Kosten
- **Skalierbarkeit**: Berücksichtigung von Unternehmensgrößeneffekten

---

## 4. Technische Architektur

### 4.1 Python-Simulator (`factory_simulator.py`)

#### Kernklassen:

**GameParameters**
```python
@dataclass
class GameParameters:
    base_sales_price: float = 13.0
    base_material_price: float = 3.0
    base_production_cost: float = 3.0
    base_assembly_cost: float = 1.0
    base_overhead_cost: float = 6.0
    marketing_budget: float = 0.0
    price_elasticity: float = 0.15
    marketing_effectiveness: float = 0.08
    # ... weitere Parameter
```

**FactorySimulator**
- Hauptsimulationsengine
- Verwaltung von Inventar, Kasse, Forderungen
- Quartalsweise Simulation
- Ergebnisberechnung und Export

**QuarterResult**
- Datenstruktur für Quartalsergebnisse
- Vollständige Dokumentation aller Kennzahlen

#### Hauptmethoden:

```python
def calculate_demand(sales_price, marketing_spend) -> int
def calculate_production_cost(lots) -> float
def simulate_quarter(sales_price, marketing_budget, production_lots, ...) -> QuarterResult
def get_summary() -> Dict
def export_results(filename) -> str
```

### 4.2 Web-Anwendung (`app.py`)

**Flask-basierte Web-API**
- `/` - Haupt-Interface (HTML)
- `/api/start_game` - Spielinitialisierung
- `/api/simulate_quarter` - Quartalssimulation
- `/api/get_summary` - Ergebniszusammenfassung
- `/api/export_results` - JSON-Export

**Frontend** (`templates/index.html`)
- Responsive Design
- Echtzeit-Statusanzeige
- Interaktive Entscheidungseingabe
- Ergebnisvisualisierung

### 4.3 Excel-Tool (`excel_generator.py`)

**Tabellenblätter:**
1. **Anleitung** - Vollständige Spielanleitung
2. **Parameter** - Konfigurierbare Spielparameter
3. **Quartal 1-4** - Interaktive Quartalsblätter
4. **Jahresabschluss** - Zusammenfassung und Kennzahlen

**Features:**
- Automatische Berechnungen mit Excel-Formeln
- Farbcodierte Eingabe- und Ausgabefelder
- Verknüpfte Quartale (Endbestand → Anfangsbestand)
- Zusammenfassende Kennzahlen

---

## 5. Benutzungsanleitung

### 5.1 Python-Kommandozeilenversion

```bash
cd planspiel_bwl
python3 factory_simulator.py
```

**Interaktiver Ablauf:**
1. Spiel startet automatisch
2. Für jedes Quartal werden Entscheidungen abgefragt:
   - Verkaufspreis eingeben (oder Enter für Standard)
   - Marketing-Budget eingeben
   - Produktionsmenge eingeben
3. Ergebnisse werden nach jedem Quartal angezeigt
4. Am Ende: Jahresabschluss und JSON-Export

### 5.2 Web-Version

```bash
cd planspiel_bwl
pip install flask --break-system-packages
python3 app.py
```

Browser öffnen: `http://localhost:5000`

**Bedienung:**
1. Klick auf "Spiel Starten"
2. Entscheidungen in Eingabefelder eingeben
3. "Quartal Simulieren" klicken
4. Ergebnisse werden angezeigt
5. Nach 4 Quartalen: "Ergebnisse Exportieren"

### 5.3 Excel-Version

```bash
cd planspiel_bwl
python3 excel_generator.py
```

Öffnen Sie `Factory_Simulation_Interactive.xlsx` mit Excel oder LibreOffice.

**Bedienung:**
1. Lesen Sie das Tabellenblatt "Anleitung"
2. Passen Sie ggf. "Parameter" an
3. Gehen Sie zu "Quartal 1"
4. Geben Sie Entscheidungen in gelb markierte Felder ein
5. Ergebnisse werden automatisch berechnet (grüne Felder)
6. Wiederholen Sie für Quartale 2-4
7. Prüfen Sie "Jahresabschluss" für Gesamtergebnis

---

## 6. Formeln und Berechnungen

### 6.1 Nachfrageberechnung

**Grundformel:**
```
Nachfrage = Basisnachfrage × Preiseffekt × Marketing-Effekt × Wettbewerbseffekt
```

**Preiseffekt:**
```
Preiseffekt = 1 - (Verkaufspreis/Basispreis - 1) × Preiselastizität
```

Beispiel:
- Basispreis = 13 M, Verkaufspreis = 14 M
- Preiselastizität = 0.15
- Preiseffekt = 1 - (14/13 - 1) × 0.15 = 1 - 0.0769 × 0.15 = 0.988

**Marketing-Effekt:**
```
Marketing-Effekt = 1 + (Marketing-Budget × Marketing-Effektivität)
```

Beispiel:
- Marketing-Budget = 2 M
- Effektivität = 0.08
- Marketing-Effekt = 1 + (2 × 0.08) = 1.16

**Wettbewerbseffekt:**
```
Wenn Verkaufspreis > Wettbewerberpreis: Faktor = 0.85
Wenn Verkaufspreis < Wettbewerberpreis: Faktor = 1.15
Sonst: Faktor = 1.0
```

### 6.2 Kostenberechnung

**Materialkosten:**
```
Materialkosten = Anzahl_Lose × Basispreis × Marktfaktor
```

**Fertigungskosten:**
```
Fertigungskosten = Anzahl_Lose × Basiskosten × Effizienzfaktor × Qualitätsfaktor
```

**Montagekosten:**
```
Montagekosten = Anzahl_Lose × Basis_Montagekosten
```

**Gesamtkosten:**
```
Gesamtkosten = Materialkosten + Fertigungskosten + Montagekosten + 
               Gemeinkosten + Marketing
```

### 6.3 Gewinnberechnung

**Bruttogewinn:**
```
Bruttogewinn = Umsatz - (Materialkosten + Fertigungskosten + Montagekosten)
```

**Nettogewinn:**
```
Nettogewinn = Umsatz - Gesamtkosten
```

**Umsatzrendite:**
```
Umsatzrendite (%) = (Gesamtgewinn / Gesamtumsatz) × 100
```

### 6.4 Liquiditätsberechnung

**Cash Flow pro Quartal:**
```
Kasse_Ende = Kasse_Anfang + Forderungen_Eingang - Gesamtausgaben

Wobei:
- Forderungen_Eingang = Forderungen vom Vorquartal
- Gesamtausgaben = Alle Kosten des aktuellen Quartals
```

**Neue Forderungen:**
```
Forderungen_neu = Umsatz_aktuelles_Quartal
```

### 6.5 Bestandsführung

**Rohmaterial:**
```
Bestand_Ende = Bestand_Anfang + Lieferung - Verbrauch
(Standardlieferung = 2 Lose pro Quartal)
```

**Halbfertigware:**
```
Bestand_Ende = Bestand_Anfang + Produktion - Montage
```

**Fertigware:**
```
Bestand_Ende = Bestand_Anfang + Montage - Verkauf
```

---

## 7. Installation und Ausführung

### 7.1 Systemanforderungen

**Mindestanforderungen:**
- Python 3.8 oder höher
- 100 MB freier Speicherplatz
- Webbrowser (für Web-Version)
- Excel oder LibreOffice (für Excel-Version)

**Python-Pakete:**
```bash
pip install flask openpyxl --break-system-packages
```

### 7.2 Projektstruktur

```
planspiel_bwl/
├── factory_simulator.py       # Hauptsimulator
├── app.py                      # Flask Web-App
├── excel_generator.py          # Excel-Generator
├── templates/
│   └── index.html             # Web-Interface
├── static/                    # Statische Dateien (CSS, JS)
├── Factory_Simulation_Interactive.xlsx  # Generierte Excel-Datei
├── factory_results.json       # Exportierte Ergebnisse
└── README.md                  # Diese Dokumentation
```

### 7.3 Schnellstart

**Option 1: Kommandozeile**
```bash
python3 factory_simulator.py
```

**Option 2: Web-Interface**
```bash
python3 app.py
# Öffnen Sie http://localhost:5000 im Browser
```

**Option 3: Excel**
```bash
python3 excel_generator.py
# Öffnen Sie Factory_Simulation_Interactive.xlsx
```

---

## 8. Beispielszenarien

### 8.1 Szenario 1: Aggressive Preisstrategie

**Strategie:** Hohe Preise, wenig Marketing

**Quartalsweise Entscheidungen:**
- Q1: Preis = 15 M, Marketing = 0 M, Produktion = 2 Lose
- Q2: Preis = 14.5 M, Marketing = 0 M, Produktion = 2 Lose
- Q3: Preis = 14 M, Marketing = 0 M, Produktion = 2 Lose
- Q4: Preis = 14 M, Marketing = 0 M, Produktion = 2 Lose

**Erwartetes Ergebnis:**
- Hohe Margen pro Einheit
- Reduzierte Absatzmenge
- Möglicherweise negativer Gesamtgewinn bei zu hohen Preisen

### 8.2 Szenario 2: Marketing-Offensive

**Strategie:** Moderate Preise, hohes Marketing

**Quartalsweise Entscheidungen:**
- Q1: Preis = 13 M, Marketing = 2 M, Produktion = 3 Lose
- Q2: Preis = 13 M, Marketing = 2.5 M, Produktion = 3 Lose
- Q3: Preis = 13 M, Marketing = 2 M, Produktion = 3 Lose
- Q4: Preis = 13.5 M, Marketing = 1 M, Produktion = 2 Lose

**Erwartetes Ergebnis:**
- Erhöhte Absatzmengen
- Höhere Gesamtkosten durch Marketing
- Marktanteilsgewinn

### 8.3 Szenario 3: Kostenführerschaft

**Strategie:** Niedrige Preise, hohe Menge

**Quartalsweise Entscheidungen:**
- Q1: Preis = 11 M, Marketing = 0.5 M, Produktion = 3 Lose
- Q2: Preis = 11.5 M, Marketing = 0.5 M, Produktion = 3 Lose
- Q3: Preis = 12 M, Marketing = 0 M, Produktion = 2 Lose
- Q4: Preis = 12 M, Marketing = 0 M, Produktion = 2 Lose

**Erwartetes Ergebnis:**
- Hohe Absatzmengen
- Niedrigere Margen
- Starke Marktposition

### 8.4 Szenario 4: Balanced Approach

**Strategie:** Ausgewogene Entscheidungen

**Quartalsweise Entscheidungen:**
- Q1: Preis = 13 M, Marketing = 1 M, Produktion = 2 Lose
- Q2: Preis = 13.5 M, Marketing = 1 M, Produktion = 2 Lose
- Q3: Preis = 13 M, Marketing = 1.5 M, Produktion = 2 Lose
- Q4: Preis = 13.5 M, Marketing = 0.5 M, Produktion = 2 Lose

**Erwartetes Ergebnis:**
- Stabile Absatzmengen
- Gute Balance zwischen Kosten und Erlösen
- Konsistenter Gewinn

---

## 9. Kennzahlen und Auswertung

### 9.1 Wichtige Kennzahlen

**Umsatzkennzahlen:**
- Gesamtumsatz (über alle Quartale)
- Durchschnittlicher Umsatz pro Quartal
- Umsatzwachstum

**Kostenkennzahlen:**
- Gesamtkosten
- Kostenstruktur (Material/Fertigung/Overhead)
- Kosten pro produzierter Einheit

**Rentabilitätskennzahlen:**
- Bruttogewinn
- Nettogewinn
- Umsatzrendite (ROS = Return on Sales)
- Durchschnittlicher Gewinn pro Quartal

**Liquiditätskennzahlen:**
- Kassenbestand am Jahresende
- Forderungen
- Liquiditätsentwicklung

### 9.2 Erfolgsbeurteilung

**Sehr gut:**
- Nettogewinn > 30 M
- Umsatzrendite > 20%
- Positive Entwicklung über alle Quartale

**Gut:**
- Nettogewinn 15-30 M
- Umsatzrendite 10-20%
- Stabile Liquidität

**Befriedigend:**
- Nettogewinn 5-15 M
- Umsatzrendite 5-10%
- Ausreichende Liquidität

**Verbesserungswürdig:**
- Nettogewinn < 5 M
- Umsatzrendite < 5%
- Liquiditätsprobleme

---

## 10. Erweiterungsmöglichkeiten

### 10.1 Geplante Erweiterungen
- Mehrere Produktvarianten
- Investitionen in Kapazitätserweiterung
- Kreditaufnahme mit Zinsen
- Lagerkosten
- Qualitätsmanagement

### 10.2 Technische Verbesserungen
- Datenbank-Integration
- Multi-User-Support
- Erweiterte Visualisierungen (Charts)
- Mobile App
- Cloud-Deployment

---

## 11. Kontakt und Support

**Entwickelt für:**
Ostfalia Hochschule für angewandte Wissenschaften  
Fakultät Maschinenbau  
Institut für Produktionstechnik

**Betreuer:**
Prof. Dr. C. Haats

**Zeitraum:**
WiSe 2025/26 (KW 45 - KW 51)

---

## 12. Lizenz und Nutzung

Dieses Projekt wurde im Rahmen der Lehrveranstaltung "Grundlagen der Betriebswirtschaftslehre" entwickelt und dient ausschließlich zu Bildungszwecken.

**Verwendung:**
- ✅ Bildungszwecke
- ✅ Nicht-kommerzielle Nutzung
- ✅ Weiterentwicklung durch Studierende
- ❌ Kommerzielle Nutzung ohne Genehmigung

---

## Anhang A: Glossar

**Begriffe:**
- **M (Münzen)**: Währungseinheit im Spiel
- **Los**: Produktionseinheit (enthält mehrere Stück)
- **Quartal**: Zeiteinheit (3 Monate)
- **Preiselastizität**: Änderung der Nachfrage bei Preisänderung
- **Gemeinkosten**: Fixe Kosten (Verwaltung, Vertrieb, F&E)
- **Halbfertigware/WIP**: Work In Progress, teilweise fertiggestellte Produkte
- **Forderungen**: Noch nicht bezahlte Rechnungen

---

**Version:** 1.0  
**Datum:** November 2025  
**Status:** Abgeschlossen
