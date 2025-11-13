# Factory Business Simulation - Schnellstart

## 🚀 Projektübersicht

**Status:** ✅ Vollständig abgeschlossen  
**Zeitplan:** Woche 46 (KW 46) - Gemäß Ihrem Projektplan  
**Nächster Schritt:** Woche 47-48 für weitere Tests und Verfeinerungen

---

## 📦 Was wurde erstellt?

### 1. **Python-Simulator** (`factory_simulator.py`)
- Vollständige Spiellogik mit variablen Parametern
- Interaktive Kommandozeilenversion
- JSON-Export der Ergebnisse
- **Verwendung:** `python3 factory_simulator.py`

### 2. **Web-Anwendung** (`app.py` + `templates/index.html`)
- Modernes, benutzerfreundliches Web-Interface
- Responsive Design
- Echtzeit-Berechnungen
- **Verwendung:** `python3 app.py` → Browser: http://localhost:5000

### 3. **Excel-Tool** (`excel_generator.py`)
- Vollautomatische Excel-Arbeitsmappe
- Interaktive Formeln
- Offline verfügbar
- **Verwendung:** `python3 excel_generator.py` → Öffne .xlsx Datei

### 4. **Demo-Skript** (`demo.py`)
- Vordefinierte Szenarien zum Testen
- Automatischer Szenario-Vergleich
- **Verwendung:** 
  - `python3 demo.py` (einzelnes Szenario)
  - `python3 demo.py --compare` (alle Szenarien vergleichen)

### 5. **Dokumentation**
- `README.md` - Umfassende technische Dokumentation (Deutsch)
- `Planspiel_BWL_Praesentation.pdf` - Präsentation für KW 50
- Diese Datei - Schnellstart-Anleitung

---

## 🎯 Hauptfeatures (alle Anforderungen erfüllt)

✅ **Variable Verkaufspreise**
   - Nachfrageelastizität implementiert
   - Wettbewerbseffekte berücksichtigt

✅ **Marketing-Budget**
   - Nachfragesteigerung durch Marketing-Ausgaben
   - Konfigurierbare Effektivität

✅ **Variable Fertigungskosten**
   - Effizienzfaktoren
   - Qualitätsfaktoren

✅ **Variable Einkaufspreise**
   - Marktfaktoren für Materialpreise
   - Realistische Preisschwankungen

✅ **Variable Gemeinkosten**
   - Anpassbare Overhead-Kosten
   - Skalierungseffekte

✅ **IT-Unterstützung**
   - 3 verschiedene Lösungen
   - Prototypisch umgesetzt und getestet

---

## ⚡ Schnellstart

### Option 1: Python Kommandozeile (am schnellsten)
```bash
cd planspiel_bwl
python3 factory_simulator.py
```
Folgen Sie den Anweisungen auf dem Bildschirm.

### Option 2: Web-Interface (am benutzerfreundlichsten)
```bash
cd planspiel_bwl
pip install flask --break-system-packages
python3 app.py
```
Öffnen Sie http://localhost:5000 in Ihrem Browser.

### Option 3: Excel (am vertrautesten)
```bash
cd planspiel_bwl
python3 excel_generator.py
```
Öffnen Sie die erstellte `Factory_Simulation_Interactive.xlsx` Datei.

### Option 4: Demo ausführen (zum Testen)
```bash
cd planspiel_bwl
python3 demo.py
python3 demo.py --compare  # Vergleicht alle 4 Szenarien
```

---

## 📊 Beispielergebnisse

Das System wurde mit 4 verschiedenen Strategien getestet:

| Szenario | Umsatz | Kosten | Gewinn | ROS % |
|----------|--------|--------|--------|-------|
| **Balanced** | 106 M | 84 M | 22 M | 20.75% |
| **Aggressive Pricing** | 115 M | 80.5 M | **34.5 M** | **30%** |
| **Marketing Focus** | 105 M | 99.5 M | 5.5 M | 5.24% |
| **Cost Leadership** | 93 M | 89 M | 4 M | 4.30% |

**Beste Strategie:** Aggressive Pricing (höchster Gewinn und ROS)

---

## 📁 Projektstruktur

```
planspiel_bwl/
├── factory_simulator.py              # Hauptsimulator
├── app.py                             # Flask Web-App
├── excel_generator.py                 # Excel-Generator
├── demo.py                            # Demo & Tests
├── create_presentation.py             # PDF-Generator
├── templates/
│   └── index.html                     # Web-Interface
├── Factory_Simulation_Interactive.xlsx # Excel-Tool
├── Planspiel_BWL_Praesentation.pdf    # Präsentation
├── README.md                          # Vollständige Doku
├── SCHNELLSTART.md                    # Diese Datei
└── requirements.txt                   # Python-Pakete
```

---

## 🔧 Technische Details

### Verwendete Technologien
- **Python 3.8+** - Programmiersprache
- **Flask** - Web-Framework
- **openpyxl** - Excel-Manipulation
- **reportlab** - PDF-Generierung

### Installation der Abhängigkeiten
```bash
pip install flask openpyxl reportlab --break-system-packages
```

### Systemanforderungen
- Python 3.8 oder höher
- 100 MB freier Speicherplatz
- Webbrowser (Chrome, Firefox, Safari, Edge)
- Optional: Excel oder LibreOffice

---

## 📅 Zeitplan (für Ihr Projekt)

**✅ Woche 46 (FERTIG):**
- ✅ Konzept definiert
- ✅ Formeln implementiert
- ✅ Alle drei IT-Lösungen erstellt
- ✅ Dokumentation geschrieben

**Woche 47-48 (EMPFOHLEN):**
- Testen Sie alle drei Versionen
- Probieren Sie verschiedene Szenarien
- Sammeln Sie Feedback von Kommilitonen
- Optimieren Sie ggf. Parameter

**Woche 49:**
- Bereiten Sie Ihre Präsentation vor
- Nutzen Sie die bereitgestellte PDF-Präsentation
- Üben Sie die Live-Demo

**Woche 50:**
- Präsentation und Testing (laut Aufgabenstellung)
- Live-Vorführung des Tools

**Woche 51:**
- Abgabe Tools und Kurzdoku (laut Aufgabenstellung)

---

## 🎓 Für die Präsentation (KW 50)

### Was Sie zeigen sollten:

1. **Problem:** 
   - Ursprüngliches Factory-Spiel war statisch
   - Fehlende Variabilität und Interaktivität

2. **Lösung:**
   - Variable Parameter implementiert
   - Drei verschiedene IT-Lösungen erstellt
   - Realistische Wirtschaftssimulation

3. **Live-Demo:**
   - Zeigen Sie das Web-Interface (am beeindruckendsten)
   - Führen Sie ein Quartal live durch
   - Zeigen Sie wie Parameter die Ergebnisse beeinflussen

4. **Ergebnisse:**
   - Zeigen Sie den Szenario-Vergleich
   - Erklären Sie die Formeln
   - Demonstrieren Sie verschiedene Strategien

5. **Technical Stack:**
   - Python für Logik
   - Flask für Web-Interface
   - Excel für Offline-Nutzung

### Vorbereitung:
```bash
# Terminal 1: Web-Server starten
cd planspiel_bwl
python3 app.py

# Terminal 2: Demo zum Vergleich bereit haben
python3 demo.py --compare
```

---

## 💡 Tipps für die Nutzung

### Für optimale Ergebnisse:
1. **Preisstrategie:** Moderate Preiserhöhungen (13-14 M) bringen gute Balance
2. **Marketing:** 1-1.5 M pro Quartal ist effektiv
3. **Produktion:** 2-3 Lose je nach Nachfrage
4. **Liquidität:** Behalten Sie die Kasse im Auge (mindestens 20 M)

### Häufige Fehler:
- ❌ Zu hohe Preise (>15 M) → Nachfrage bricht ein
- ❌ Zu viel Marketing ohne Preisanpassung → Kosten zu hoch
- ❌ Überproduktion → Lagerbestände steigen, Liquidität sinkt
- ❌ Zu niedrige Preise (<11 M) → Gewinnmarge zu niedrig

---

## 🆘 Problemlösung

### Problem: Flask startet nicht
```bash
pip install flask --break-system-packages
```

### Problem: Excel-Datei öffnet nicht
- Stellen Sie sicher, dass openpyxl installiert ist:
```bash
pip install openpyxl --break-system-packages
```

### Problem: "ModuleNotFoundError"
- Installieren Sie alle Abhängigkeiten:
```bash
cd planspiel_bwl
pip install -r requirements.txt --break-system-packages
```

---

## ✅ Checkliste für Abgabe (KW 51)

**Dateien zum Einreichen:**
- [ ] `factory_simulator.py` - Hauptsimulator
- [ ] `app.py` + `templates/` - Web-Version
- [ ] `excel_generator.py` - Excel-Version
- [ ] `README.md` - Technische Dokumentation
- [ ] `Planspiel_BWL_Praesentation.pdf` - Präsentation
- [ ] `Factory_Simulation_Interactive.xlsx` - Beispiel-Excel

**Optional aber empfohlen:**
- [ ] `demo.py` - Demonstrationsskript
- [ ] Screenshots des Web-Interfaces
- [ ] Beispiel-Ergebnisdateien (JSON)

---

## 🎉 Gratulation!

Sie haben erfolgreich:
- ✅ Alle Anforderungen implementiert
- ✅ Drei verschiedene IT-Lösungen erstellt
- ✅ Umfassende Dokumentation geschrieben
- ✅ Testszenarien durchgeführt

Das Projekt ist **vollständig fertig** und bereit für:
- Präsentation in Woche 50
- Abgabe in Woche 51

---

## 📞 Nächste Schritte

1. **Testen Sie alle drei Versionen**
   ```bash
   python3 factory_simulator.py
   python3 app.py
   python3 excel_generator.py
   python3 demo.py --compare
   ```

2. **Lesen Sie die vollständige Dokumentation**
   - Öffnen Sie `README.md` für technische Details
   - Öffnen Sie `Planspiel_BWL_Praesentation.pdf` für Präsentation

3. **Bereiten Sie Ihre Präsentation vor**
   - Üben Sie die Live-Demo
   - Verstehen Sie die Formeln
   - Kennen Sie die Ergebnisse

4. **Wöchentliche Rücksprachen (KW 46-49)**
   - Zeigen Sie Ihren Fortschritt
   - Holen Sie Feedback ein
   - Optimieren Sie bei Bedarf

---

**Viel Erfolg! 🚀**

Bei Fragen zur Implementierung oder Bedienung, schauen Sie in die `README.md` 
oder führen Sie `python3 demo.py --compare` aus, um alle Features zu sehen.
