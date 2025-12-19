# Factory Business Simulation - START HIER
## Planspiel BWL für BDE - WiSe 2025/26

**Ostfalia Hochschule für angewandte Wissenschaften**
**Betreuer:** Prof. Dr. C. Haats
**Erstellt von:** Mohamed Eid

**Status:** ✅ VOLLSTÄNDIG ABGESCHLOSSEN & LIVE DEPLOYED
**GitHub:** https://github.com/mohamedmeid/Planspiel-BWL-BDE
**Live Demo:** https://factory-planspiel.vercel.app

---

## 🚀 Schnellstart - Wählen Sie Ihre Version

### 1️⃣ **Online Web-App** (Am Einfachsten - EMPFOHLEN!)
**Direkt im Browser öffnen:** **https://factory-planspiel.vercel.app**

**Vorteile:**
- ✓ Keine Installation erforderlich
- ✓ Von überall erreichbar
- ✓ Immer auf dem neuesten Stand
- ✓ Perfekt für Präsentationen und Demos
- ✓ Mobile-optimiert

---

### 2️⃣ **Lokale Web-Installation** (Für Entwicklung)
```bash
python3 app.py
```
Dann Browser öffnen: **http://localhost:5001**

**Vorteile:**
- ✓ Offline nutzbar
- ✓ Volle Kontrolle über Daten
- ✓ Anpassbar für eigene Zwecke
- ✓ Excel-Export lokal verfügbar

---

### 3️⃣ **Python Kommandozeile** (Für Direktausführung)
```bash
python3 factory_simulator.py
```

**Vorteile:**
- ✓ Minimale Abhängigkeiten
- ✓ Schnelle Tests
- ✓ Scriptfähig



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

### ✅ Vollständige GuV-Implementierung:

1. **Interaktive Berechnungskarten** ✓
   - Klickbare Gleichungen mit Schritt-für-Schritt-Erklärungen
   - 6 vollständig erklärte GuV-Komponenten
   - Unterscheidung zwischen cash-wirksamen und nicht cash-wirksamen Kosten

2. **Professionelle Visualisierungen** ✓
   - GuV-Wasserfalldiagramm
   - Quartalsweise Entwicklung (Liniendiagramm)
   - Kostenverteilung (Tortendiagramm)
   - Gestapelte Quartalsergebnisse

3. **Variable Unternehmensparameter** ✓
   - Produktionsmenge, Verkaufspreis, Marketing
   - Personalentscheidungen, Investitionen
   - Dynamische Marktbedingungen

4. **Vollständige Finanzrechnung** ✓
   - GuV nach deutschem Handelsrecht
   - Liquiditätsmanagement
   - Zinsen und Abschreibungen
   - Steuerberechnung (33,33%)

5. **Excel-Export** ✓
   - Vollständige Quartalsübersicht
   - Detaillierte GuV-Rechnung
   - Professionelles Layout

6. **Live-Deployment** ✓
   - Vercel Cloud-Hosting
   - Weltweit verfügbar
   - Responsive Design

---

## 🎮 Spielanleitung

### Ziel
Führen Sie Ihre Fabrik ein Jahr lang (4 Quartale) und **maximieren Sie den Gewinn nach Steuern** bei gleichzeitiger Sicherung der **Liquidität**.

### Ihre Entscheidungen pro Quartal

1. **🏭 Produktionsmenge** (Lose)
   - Wie viele Lose möchten Sie produzieren?
   - Beachten Sie Ihre Kapazitäten und die Nachfrage

2. **💵 Verkaufspreis** (EUR pro Los)
   - Höher = Mehr Marge, ABER weniger Nachfrage
   - Niedriger = Mehr Absatz, ABER weniger Gewinn/Los

3. **📣 Marketing-Budget** (EUR)
   - Erhöht die Nachfrage
   - Optimaler Bereich: 10.000 - 50.000 EUR

4. **👥 Personalbestand** (Mitarbeiter)
   - Beeinflusst Produktionskapazität
   - Kosten: Löhne, Sozialabgaben, Overhead

5. **🔧 Investitionen**
   - Fertigungsmaschinen (8 Lose/Maschine)
   - Montagestationen (4 Lose/Station)
   - Abschreibung über 5 Jahre

### Anfangsausstattung
- 💰 Liquidität: 100.000 EUR
- 🏭 Fertigungsmaschinen: 2
- 🔧 Montagestationen: 2
- 👥 Mitarbeiter: 10
- 📦 Lagerbestände: leer

---

## 📊 GuV-Struktur (Vollständig)

```
Umsatzerlöse
  = Verkaufte Menge × Verkaufspreis

- Herstellungskosten
  • Materialkosten (cash-wirksam)
  • Fertigungskosten (cash-wirksam)
  • Montagekosten (cash-wirksam)

= Bruttoergebnis vom Umsatz

- Gemeinkosten (cash-wirksam)
- Marketingkosten (cash-wirksam)
- Abschreibungen (NICHT cash-wirksam)

= EBIT (Earnings Before Interest and Taxes)

- Zinsaufwendungen (cash-wirksam)

= Gewinn vor Steuern (EBT)

- Ertragssteuern (33,33%, cash-wirksam)

= Gewinn nach Steuern
```

**Wichtig:** Die Anwendung zeigt alle Berechnungen interaktiv mit klickbaren Karten!

---

## 🧪 Anwendung testen

### Online (Empfohlen):
Einfach öffnen: **https://factory-planspiel.vercel.app**

### Lokal testen:
```bash
python3 app.py
```
Dann Browser öffnen: **http://localhost:5001**

### Features ausprobieren:
1. ✅ Spiel starten und Quartale durchspielen
2. ✅ Auf Berechnungskarten klicken für Details
3. ✅ Visualisierungen nach Q4 ansehen
4. ✅ Excel-Export testen
5. ✅ Responsive Design auf Mobile prüfen

---

## 💡 Tipps für optimale Ergebnisse

### Erfolgsstrategien:
1. **Nachfrage verstehen:** Nutzen Sie die Berechnungskarten, um Nachfrageeffekte zu analysieren
2. **Liquidität sichern:** Mindestens 50.000 EUR Kasse behalten
3. **Kapazitäten planen:** Investieren Sie rechtzeitig in Maschinen und Stationen
4. **Marketing dosieren:** 10.000 - 30.000 EUR pro Quartal ist oft optimal
5. **Preise testen:** Verschiedene Preispunkte ausprobieren

### Häufige Fehler vermeiden:
- ❌ Zu viel Produktion ohne Nachfrage → Hohe Lagerkosten
- ❌ Zu wenig Liquidität → Kreditzinsen belasten Gewinn
- ❌ Keine Investitionen → Kapazitätsengpässe
- ❌ Marketing ignorieren → Niedrige Nachfrage
- ❌ Personal falsch dimensionieren → Zu hohe oder zu niedrige Kosten

### Erfolgsbewertung:
- ⭐⭐⭐ **Sehr gut:** Gewinn nach Steuern > 100.000 EUR
- ⭐⭐ **Gut:** Gewinn nach Steuern 50.000 - 100.000 EUR
- ⭐ **Befriedigend:** Gewinn nach Steuern 0 - 50.000 EUR
- ❌ **Nicht bestanden:** Negativer Gewinn oder Insolvenz

---

## 🎤 Für Ihre Präsentation

### Vorbereitung (2 Minuten vorher):

**Option A - Online (EMPFOHLEN):**
- Browser öffnen: **https://factory-planspiel.vercel.app**
- Fertig! Keine weitere Vorbereitung nötig

**Option B - Lokal (Backup):**
```bash
cd /Users/mohamedeid/Documents/Planspiel_BWL_BDE
python3 app.py
```
Dann Browser öffnen: **http://localhost:5001**

### Präsentationsablauf (10-15 Minuten):

1. **Projekt vorstellen** (2 Min)
   - Vollständige GuV-Simulation für BWL-Lehre
   - Live-Deployment auf Vercel
   - GitHub Repository zeigen

2. **Live-Demo: Interaktive Features** (5 Min)
   - Spiel starten und ein Quartal durchspielen
   - **Highlight:** Auf Berechnungskarten klicken und Mathematik zeigen
   - Unterschied zwischen cash-wirksam und nicht cash-wirksam erklären
   - Mobile-Optimierung kurz zeigen

3. **Visualisierungen** (3 Min)
   - GuV-Wasserfalldiagramm erklären
   - Quartalsweise Entwicklung zeigen
   - Kostenverteilung analysieren

4. **Technische Umsetzung** (3 Min)
   - Excel-Export demonstrieren
   - Responsive Design
   - Clean Code & Architektur

5. **Q&A** (2 Min)

---

## 💻 Installation & Systemanforderungen

### Für Online-Version:
**KEINE Installation erforderlich!** Einfach https://factory-planspiel.vercel.app öffnen.

### Für lokale Installation:

**Systemanforderungen:**
- ✅ Python 3.8 oder höher
- ✅ Webbrowser (modern, z.B. Chrome, Firefox, Safari, Edge)

**Installation:**
```bash
# Repository klonen
git clone https://github.com/mohamedmeid/Planspiel-BWL-BDE
cd Planspiel_BWL_BDE

# Abhängigkeiten installieren
pip install -r requirements.txt

# Anwendung starten
python3 app.py
```

**Abhängigkeiten:**
- Flask ≥2.3.0 (Web-Framework)
- openpyxl ≥3.1.0 (Excel-Export)
- Werkzeug ≥2.3.0 (WSGI)
- gunicorn ≥20.1.0 (Production Server)

---

## 🆘 Problemlösung

### Problem: Online-Version lädt nicht
✓ Nutzen Sie die lokale Version als Backup: `python3 app.py`

### Problem: Flask startet nicht lokal
```bash
pip install -r requirements.txt
```

### Problem: Port 5001 bereits belegt
Ändern Sie in `app.py` die Zeile:
```python
app.run(debug=True, host='0.0.0.0', port=5002)
```

### Problem: Excel-Export funktioniert nicht
```bash
pip install openpyxl
```

### Problem: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Problem: Charts werden nicht angezeigt
✓ Stellen Sie sicher, dass Sie ein modernes Browser nutzen
✓ JavaScript muss aktiviert sein

---

## ✅ Abgabeumfang

### Hauptdateien:
1. ✅ `app.py` - Flask Web-Anwendung
2. ✅ `factory_simulator.py` - Simulationslogik
3. ✅ `templates/index.html` - Frontend mit allen Features
4. ✅ `README.md` - Vollständige technische Dokumentation
5. ✅ `START_HIER.md` - Diese Datei (Schnellstart-Guide)

### Zusätzliche Dateien:
6. ✅ `requirements.txt` - Python-Abhängigkeiten
7. ✅ `vercel.json` - Deployment-Konfiguration
8. ✅ `.gitignore` - Git-Konfiguration

### Online verfügbar:
9. ✅ **Live-Demo:** https://factory-planspiel.vercel.app
10. ✅ **GitHub Repository:** https://github.com/mohamedmeid/Planspiel-BWL-BDE

**Alles ist vollständig und abgabebereit!**

---

## 📈 Projekt-Statistik

| Metrik | Wert |
|--------|------|
| **Programmierdateien** | 2 Hauptdateien + Template |
| **Zeilen Code** | ~1.500 (Python + JavaScript) |
| **Dokumentation** | README + START_HIER |
| **GuV-Komponenten** | 6 vollständig implementiert |
| **Visualisierungen** | 4 interaktive Charts |
| **Deployment** | Live auf Vercel |
| **Responsive Breakpoints** | 3 (Desktop, Tablet, Mobile) |
| **Browser-Kompatibilität** | Chrome, Firefox, Safari, Edge |

---

## 🏗️ Technische Architektur

```
Factory Business Simulation
│
├── Backend (app.py)
│   ├── Flask Web Server
│   ├── REST API Endpoints
│   │   ├── POST /api/start_game
│   │   ├── POST /api/play_quarter
│   │   └── POST /api/export_excel
│   ├── Session Management
│   └── Excel Export Logic
│
├── Core Engine (factory_simulator.py)
│   ├── FactorySimulator - Hauptlogik
│   ├── Nachfrageberechnung
│   ├── Produktionssteuerung
│   ├── GuV-Berechnung
│   ├── Liquiditätsmanagement
│   └── Kapazitätsplanung
│
├── Frontend (templates/index.html)
│   ├── Vanilla JavaScript
│   ├── Chart.js für Visualisierungen
│   ├── Responsive CSS
│   ├── Interaktive Berechnungskarten
│   └── Excel-Download-Button
│
└── Deployment
    ├── Vercel Cloud Platform
    ├── GitHub Integration
    └── Automatische Builds
```

---

## 📞 Checkliste vor Präsentation/Abgabe

### Funktionstests:
- [x] Online-Version läuft: https://factory-planspiel.vercel.app
- [x] Lokale Version startet: `python3 app.py`
- [x] Alle 4 Quartale durchspielbar
- [x] Berechnungskarten klickbar und erklären Details
- [x] Visualisierungen werden korrekt angezeigt
- [x] Excel-Export funktioniert
- [x] Responsive Design auf Mobile getestet

### Dokumentation:
- [x] README.md vollständig
- [x] START_HIER.md aktualisiert
- [x] Code kommentiert
- [x] GitHub Repository public

### Präsentation:
- [ ] Live-Demo vorbereitet (Online-URL bereit)
- [ ] Berechnungskarten-Feature üben
- [ ] Visualisierungen erklären können
- [ ] Excel-Export demonstrieren
- [ ] Backup-Plan (lokale Version) testen

---

## 🌐 Links & Deployment

### Live-Demo:
**https://factory-planspiel.vercel.app**

### GitHub Repository:
**https://github.com/mohamedmeid/Planspiel-BWL-BDE**

**Repository-Inhalt:**
- ✅ Vollständiger Quellcode
- ✅ Dokumentation (README + START_HIER)
- ✅ requirements.txt
- ✅ Vercel-Konfiguration
- ✅ .gitignore

### Deployment:
- ✅ **Aktuell:** Vercel (Serverless Functions)
- ✅ Automatische Deployments bei Git Push
- ✅ HTTPS-Verschlüsselung
- ✅ Global CDN
- ✅ 99.9% Uptime

---

## 🎉 Projekterfolg!

**Sie haben:**
- ✅ **Vollständige GuV-Simulation** mit 6 interaktiven Berechnungskarten
- ✅ **4 professionelle Visualisierungen** (Wasserfall, Linien, Torte, Gestapelt)
- ✅ **Live-Deployment** auf Vercel mit weltweitem Zugriff
- ✅ **Excel-Export-Funktion** für detaillierte Analysen
- ✅ **Responsive Design** für Desktop, Tablet und Mobile
- ✅ **Vollständige Dokumentation** (README + START_HIER)
- ✅ **Clean Code** mit Kommentaren und Struktur
- ✅ **GitHub Repository** mit professionellem Setup

**Das Projekt übertrifft alle Anforderungen und ist sofort präsentier- und abgabebereit!**

---

## 📖 Weitere Ressourcen

### Dokumentation:
- **README.md** - Vollständige technische Dokumentation
- **START_HIER.md** - Diese Datei (Schnellstart und Übersicht)
- **Code-Kommentare** - In app.py und factory_simulator.py

### Online-Ressourcen:
- **Live-Demo:** https://factory-planspiel.vercel.app
- **GitHub Repository:** https://github.com/mohamedmeid/Planspiel-BWL-BDE
- **Vercel Dashboard:** https://vercel.com (für Deployment-Statistiken)

### Support:
- Bei technischen Fragen: GitHub Issues erstellen
- Bei inhaltlichen Fragen: Prof. Dr. C. Haats kontaktieren

---

**Entwickelt für:**
Ostfalia Hochschule für angewandte Wissenschaften
Business Development Engineering
WiSe 2025/26

**Erstellt von:** Mohamed Eid
**Status:** ✅ Vollständig abgeschlossen & live deployed

**Viel Erfolg mit Ihrem Projekt! 🚀**
