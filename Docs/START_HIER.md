# Factory Business Simulation - START HIER
## Planspiel BWL für BDE - WiSe 2025/26

**Ostfalia Hochschule für angewandte Wissenschaften**
**Betreuer:** Prof. Dr. C. Haats
**Erstellt von:** Mohamed Eid

**Status:** ✅ VOLLSTÄNDIG ABGESCHLOSSEN
**GitHub:** https://github.com/mohamedmeid/Planspiel-BWL-BDE

---

## 🚀 Schnellstart - Wählen Sie Ihre Version

### 1️⃣ **Web-Interface** (Empfohlen für Präsentation)
```bash
python3 app.py
```
Dann Browser öffnen: **http://localhost:5001**

**Vorteile:**
- ✓ Modernes, benutzerfreundliches Interface
- ✓ Echtzeit-Statusanzeige
- ✓ Excel-Export mit einem Klick
- ✓ "Neues Spiel" Button zum Zurücksetzen

---

### 2️⃣ **Python Kommandozeile** (Schnellste Option)
```bash
python3 factory_simulator.py
```

**Vorteile:**
- ✓ Sofort startklar, keine Installation
- ✓ Interaktiv: Entscheidungen werden abgefragt
- ✓ Automatischer JSON-Export



## 📂 Projektinhalt

### 🚀 Hauptprogramme

| Datei | Beschreibung | Verwendung |
|-------|--------------|------------|
| `app.py` | **Web-Anwendung** - Flask Server | `python3 app.py` |
| `factory_simulator.py` | **Kern-Simulator** - Spiellogik | `python3 factory_simulator.py` |
| `excel_generator.py` | **Excel-Generator** | `python3 excel_generator.py` |
| `demo.py` | **Demo-Skript** - Auto-Tests | `python3 demo.py --compare` |

### 📄 Dokumentation

| Datei | Beschreibung |
|-------|--------------|
| `README.md` | Vollständige technische Dokumentation |
| `START_HIER.md` | Diese Datei - Projektübersicht & Schnellstart |
| `Planspiel_BWL_Praesentation.pdf` | Präsentation für KW 50 |

### 📁 Verzeichnisse

| Ordner | Inhalt |
|--------|--------|
| `templates/` | HTML-Template für Web-Interface |
| `exports/` | Generierte Excel-Exporte vom Webserver |

---

## 🎯 Was wurde entwickelt?

### ✅ Alle 6 Anforderungen erfüllt:

1. **Variable Verkaufspreise** ✓
   - Preiselastizität der Nachfrage
   - Wettbewerbseffekte

2. **Variable Absatzmengen durch Marketing** ✓
   - Marketing-Budget beeinflusst Nachfrage
   - Konfigurierbare Effektivität

3. **Variable Fertigungskosten** ✓
   - Effizienzfaktoren
   - Qualitätsfaktoren

4. **Variable Einkaufspreise** ✓
   - Marktfaktoren
   - Preisschwankungen

5. **Variable Gemeinkosten** ✓
   - Anpassbare Overhead-Kosten

6. **IT-Unterstützung** ✓
   - Python-Simulator (CLI)
   - Web-Interface (Flask)
   - Excel-Tool (Offline)

---

## 🎮 Spielanleitung (Kurzfassung)

### Ziel
Führen Sie Ihre Fabrik ein Jahr lang (4 Quartale) und **maximieren Sie den Gewinn**.

### Ihre Entscheidungen pro Quartal

1. **💵 Verkaufspreis** (M pro Einheit)
   - Standard: 13.0 M
   - Höher = Mehr Gewinn/Einheit, ABER weniger Nachfrage
   - Niedriger = Mehr Nachfrage, ABER weniger Gewinn/Einheit

2. **📣 Marketing-Budget** (M)
   - Standard: 0 M
   - Mehr Marketing = Höhere Nachfrage
   - Effektivität: 0.08 (8% Nachfragesteigerung pro 1 M)

3. **🏭 Produktionsmenge** (Lose)
   - Standard: 2 Lose
   - Mehr Produktion = Können mehr verkaufen (wenn Nachfrage da ist)

4. **📊 Materialpreis-Faktor**
   - Standard: 1.0 (normal)
   - 1.2 = 20% teurer, 0.8 = 20% günstiger
   - Simuliert Marktschwankungen

### Anfangsbestand
- 💰 Kasse: 28.0 M
- 📋 Forderungen: 26.0 M
- 📦 Rohmaterial: 2 Lose
- ⚙️ Halbfertigware: 2 Lose
- 📦 Fertigware: 2 Lose

---

## 📊 Berechnungsformeln (Kurzfassung)

### Nachfrage:
```
Nachfrage = Basisnachfrage × Preiseffekt × Marketing-Effekt × Wettbewerb
```

### Preiseffekt:
```
Preiseffekt = 1 - (Verkaufspreis/13 - 1) × 0.15
```

### Marketing-Effekt:
```
Marketing-Effekt = 1 + (Marketing-Budget × 0.08)
```

### Gewinn:
```
Nettogewinn = Umsatz - (Material + Fertigung + Montage + Overhead + Marketing)
```

Vollständige Formeln siehe `README.md` Sektion 6.

---

## 🧪 Demo & Tests

### Einzelnes Szenario testen:
```bash
python3 demo.py
```
Führt automatisch ein "Balanced" Szenario durch.

### Alle Szenarien vergleichen:
```bash
python3 demo.py --compare
```
Vergleicht 4 verschiedene Strategien:
- **Balanced** - Ausgewogen
- **Aggressive Pricing** ⭐ (beste Ergebnisse: ~34.5 M Gewinn)
- **Marketing Focus** - Hohe Marketingausgaben
- **Cost Leadership** - Niedrige Preise, hohe Menge

---

## 💡 Tipps für optimale Ergebnisse

### Erfolgsstrategien:
1. **Preisstrategie:** Moderate Erhöhungen (13-14 M) bringen gute Balance
2. **Marketing:** 1-1.5 M pro Quartal ist effektiv
3. **Produktion:** 2-3 Lose je nach erwarteter Nachfrage
4. **Liquidität:** Kasse mindestens 20 M behalten

### Häufige Fehler vermeiden:
- ❌ Zu hohe Preise (>15 M) → Nachfrage bricht ein
- ❌ Zu viel Marketing ohne Preisanpassung → Kosten explodieren
- ❌ Überproduktion → Lagerbestände, niedrige Liquidität
- ❌ Zu niedrige Preise (<11 M) → Gewinnmarge zu niedrig

### Erfolgsbewertung:
- ⭐⭐⭐ **Sehr gut:** Nettogewinn > 30 M, Umsatzrendite > 20%
- ⭐⭐ **Gut:** Nettogewinn 15-30 M, Umsatzrendite 10-20%
- ⭐ **Befriedigend:** Nettogewinn 5-15 M, Umsatzrendite 5-10%

---

## 🎤 Für Ihre Präsentation (KW 50)

### Vorbereitung (5 Minuten vorher):

**Terminal 1 - Web-Server starten:**
```bash
cd /Users/mohamedeid/Documents/Planspiel_BWL_BDE
python3 app.py
```

**Terminal 2 - Demo bereit haben:**
```bash
python3 demo.py --compare
```

**Browser:**
- Öffnen Sie http://localhost:5001
- Bereiten Sie ein neues Spiel vor

### Präsentationsablauf (10-15 Minuten):

1. **Problem erklären** (2 Min)
   - Ursprüngliches Factory-Spiel war statisch
   - Fehlende Variabilität

2. **Lösung vorstellen** (3 Min)
   - Variable Parameter implementiert
   - Drei IT-Lösungen erstellt
   - Zeigen Sie GitHub Repository

3. **Live-Demo** (5 Min)
   - Web-Interface zeigen
   - 1-2 Quartale live spielen
   - Excel-Export demonstrieren

4. **Ergebnisse** (3 Min)
   - Szenario-Vergleich zeigen
   - Beste Strategie erklären
   - Excel-Tool zeigen

5. **Q&A** (2 Min)

---

## 💻 Installation & Systemanforderungen

### Systemanforderungen:
- ✅ Python 3.8 oder höher
- ✅ 100 MB freier Speicher
- ✅ Webbrowser (für Web-Version)
- ✅ Excel/LibreOffice (für Excel-Version)

### Installation:
```bash
# Alle Abhängigkeiten installieren:
pip install flask openpyxl --break-system-packages

# Oder aus requirements.txt:
pip install -r requirements.txt --break-system-packages
```

### Keine Installation nötig für:
- ✓ Python Kommandozeilenversion
- ✓ Excel-Generierung (wenn openpyxl bereits installiert)

---

## 🆘 Problemlösung

### Problem: Flask startet nicht
```bash
pip install flask --break-system-packages
```

### Problem: Port 5001 bereits belegt
Ändern Sie in `app.py` Zeile 169:
```python
app.run(debug=True, host='0.0.0.0', port=5002)
```

### Problem: Excel-Datei öffnet nicht
```bash
pip install openpyxl --break-system-packages
python3 excel_generator.py
```

### Problem: "ModuleNotFoundError"
```bash
pip install -r requirements.txt --break-system-packages
```

---

## ✅ Für Ihre Abgabe (KW 51)

### Mindestabgabe:
1. ✅ `factory_simulator.py` - Simulator
2. ✅ `app.py` + `templates/` - Web-Version
3. ✅ `excel_generator.py` - Excel-Version
4. ✅ `README.md` - Dokumentation

### Empfohlene Zusätze:
5. ✅ `demo.py` - Demonstrationsskript
6. ✅ `Factory_Simulation_Interactive.xlsx` - Beispiel-Excel
7. ✅ `Planspiel_BWL_Praesentation.pdf` - Präsentation
8. ✅ GitHub Repository Link

**Alles ist bereit für die Abgabe!**

---

## 📈 Projekt-Statistik

| Metrik | Wert |
|--------|------|
| **Programmierdateien** | 4 (.py) |
| **Zeilen Code** | ~1.200 |
| **Dokumentation** | ~10.000 Wörter |
| **Implementierte Features** | 6/6 (100%) |
| **IT-Lösungen** | 3 |
| **Test-Szenarien** | 4 |
| **GitHub Commits** | 3+ |

---

## 🏗️ Technische Architektur

```
Factory Business Simulation
│
├── Core Engine (factory_simulator.py)
│   ├── GameParameters - Spielparameter
│   ├── FactorySimulator - Hauptlogik
│   └── QuarterResult - Ergebnisstruktur
│
├── Web Interface (app.py + templates/)
│   ├── Flask REST API
│   ├── HTML/CSS/JavaScript Frontend
│   ├── Excel Export (/api/export_excel)
│   └── Session Management
│
├── Excel Tool (excel_generator.py)
│   ├── Openpyxl für Excel-Manipulation
│   ├── 6 Tabellenblätter
│   └── Automatische Formeln
│
└── Demo & Tests (demo.py)
    ├── 4 vordefinierte Szenarien
    └── Automatischer Vergleich
```

---

## 📞 Nächste Schritte

### Diese Woche (KW 46):
- [x] Projekt erstellt und getestet
- [x] Auf GitHub hochgeladen
- [ ] Alle drei Versionen selbst ausprobieren
- [ ] Excel-Export testen

### KW 47-48:
- [ ] Weitere Tests durchführen
- [ ] Feedback von Kommilitonen einholen
- [ ] Parameter ggf. optimieren
- [ ] Präsentation vorbereiten

### KW 49:
- [ ] Präsentation üben
- [ ] Live-Demo vorbereiten
- [ ] Beide Terminals testen

### KW 50:
- [ ] **Präsentation**
- [ ] Live-Vorführung

### KW 51:
- [ ] **Abgabe** aller Dateien
- [ ] GitHub Link einreichen

---

## 🌐 GitHub Repository

**Repository:** https://github.com/mohamedmeid/Planspiel-BWL-BDE

**Was ist enthalten:**
- ✅ Alle Python-Dateien
- ✅ Web-Templates
- ✅ Dokumentation
- ✅ Excel-Template
- ✅ Präsentation PDF
- ✅ .gitignore (sauberes Repository)

**Für Deployment:**
- Kann auf Replit gehostet werden
- Kann auf PythonAnywhere deployed werden
- Kann auf Render.com deployed werden

---

## 🎉 Erfolg!

**Sie haben jetzt:**
- ✅ Ein vollständig funktionierendes Business-Simulationsspiel
- ✅ Drei verschiedene Nutzungsmöglichkeiten
- ✅ Professionelles GitHub Repository
- ✅ Umfassende Dokumentation
- ✅ Fertige Präsentation
- ✅ Alle Anforderungen zu 100% erfüllt

**Das Projekt ist abgabebereit!**

---

## 📖 Weiterführende Informationen

- **Technische Details:** Siehe `README.md`
- **Präsentation:** Siehe `Planspiel_BWL_Praesentation.pdf`
- **Code-Dokumentation:** Kommentare in .py Dateien
- **GitHub:** https://github.com/mohamedmeid/Planspiel-BWL-BDE

---

**Entwickelt für:**
Ostfalia Hochschule für angewandte Wissenschaften
Fakultät Maschinenbau
Institut für Produktionstechnik
WiSe 2025/26
**Viel Erfolg mit Ihrem Projekt! 🚀**
