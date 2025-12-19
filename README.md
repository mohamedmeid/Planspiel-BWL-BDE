# Factory Business Simulation - Planspiel BWL für BDE

Eine interaktive Webanwendung zur Simulation einer Fabrikgeschäftstätigkeit mit vollständiger Gewinn- und Verlustrechnung (GuV), entwickelt für das Modul Business Development Engineering.

**Live-Demo:** https://factory-planspiel.vercel.app

## Übersicht

Diese Anwendung simuliert ein vierquartaliges Geschäftsjahr einer produzierenden Fabrik. Studierende treffen betriebswirtschaftliche Entscheidungen und sehen die finanziellen Auswirkungen in Echtzeit durch interaktive Berechnungen und professionelle Visualisierungen.

## Hauptfunktionen

### Interaktive Berechnungskarten
- Klickbare Gleichungskarten zeigen die Mathematik hinter jeder Berechnung
- Schritt-für-Schritt-Erklärungen aller GuV-Posten
- Visuelle Unterscheidung zwischen cash-wirksamen und nicht cash-wirksamen Kosten
- 6 vollständig erklärte Berechnungen: Umsatzerlöse, Herstellungskosten, Bruttoergebnis, EBIT, Gewinn vor Steuern, Gewinn nach Steuern

### Quartalsweise Simulation
- 4 Quartale pro Spielsession
- Entscheidungen zu: Produktionsmenge, Verkaufspreis, Marketing, Personal, Investitionen
- Dynamische Marktbedingungen mit Nachfrage- und Wettbewerbseffekten
- Echtzeit-Berechnung aller Finanzkennzahlen

### Professionelle Visualisierungen
- **GuV-Wasserfalldiagramm**: Vollständige Darstellung der Gewinn- und Verlustrechnung vom Umsatz bis zum Nettogewinn
- **Quartalsweise Entwicklung**: Liniendiagramm mit Umsatz, Kosten, Gewinn und Liquidität
- **Kostenverteilung**: Tortendiagramm zur Analyse der Kostenstruktur
- **Gestapelte Quartalsergebnisse**: Vergleich aller Quartale mit detaillierter Kostenaufschlüsselung

### Vollständige GuV-Implementierung
```
Umsatzerlöse
- Herstellungskosten (Material, Fertigung, Montage)
= Bruttoergebnis vom Umsatz
- Gemeinkosten
- Marketingkosten
- Abschreibungen (nicht cash-wirksam)
= EBIT
- Zinsen
= Gewinn vor Steuern
- Steuern (33,33%)
= Gewinn nach Steuern
```

## Zugriff auf die Anwendung

### Online (Empfohlen)
Die Anwendung ist live auf Vercel verfügbar:
**https://factory-planspiel.vercel.app**

Keine Installation erforderlich - einfach den Link öffnen und loslegen!

### Lokale Installation

#### Voraussetzungen
- Python 3.8+
- Flask
- openpyxl

#### Schnellstart

```bash
# Repository klonen
git clone [repository-url]
cd Planspiel_BWL_BDE

# Abhängigkeiten installieren
pip install -r requirements.txt

# Anwendung starten
python3 app.py

# Im Browser öffnen
http://localhost:5001
```

## Verwendung

1. **Spiel starten**: Klicken Sie auf "Spiel Starten", um eine neue Session zu beginnen
2. **Entscheidungen treffen**: Geben Sie für jedes Quartal Ihre Unternehmensentscheidungen ein
3. **Quartal simulieren**: Sehen Sie die finanziellen Ergebnisse in Echtzeit
4. **Berechnungen erkunden**: Klicken Sie auf beliebige Gleichungskarten, um die Mathematik dahinter zu verstehen
5. **Analysen durchführen**: Nach Quartal 4 werden automatisch alle Visualisierungen angezeigt
6. **Ergebnisse exportieren**: Laden Sie eine vollständige Excel-Datei mit allen Quartalen herunter

## Technische Details

### Architektur
- **Backend**: Flask (Python)
- **Frontend**: Vanilla JavaScript, Chart.js
- **Styling**: Modernes CSS mit Animationen und responsivem Design
- **Export**: openpyxl für Excel-Generierung
- **Deployment**: Vercel

### Berechnungslogik
- Dynamische Nachfrageberechnung basierend auf Preis und Marketing
- Kapazitätsplanung mit Fertigungsmaschinen und Montagestationen
- Lagerverwaltung mit FIFO-Prinzip
- Zinsberechnung auf Kredite und Einlagen
- Abschreibungen auf Anlagegüter (5 Jahre linear)

### Responsive Design
- Vollständig optimiert für Desktop, Tablet und Mobile
- Touch-optimierte Bedienelemente
- Adaptive Layouts für alle Bildschirmgrößen

## Projektstruktur

```
Planspiel_BWL_BDE/
├── app.py                  # Flask-Anwendung
├── factory_simulator.py    # Simulationslogik
├── templates/
│   └── index.html         # Haupttemplate mit UI
├── exports/               # Generierte Excel-Dateien
├── requirements.txt       # Python-Abhängigkeiten
└── README.md             # Diese Datei
```

## Features für Lernerfahrung

- **Interaktives Lernen**: Jede Berechnung wird mit Formeln und Zwischenschritten erklärt
- **Visuelle Feedbacks**: Farbcodierung zeigt positive/negative Entwicklungen
- **Kontextuelle Hinweise**: Tooltips erklären wichtige Konzepte wie cash-wirksame vs. nicht cash-wirksame Kosten
- **Praxisnähe**: Realistische Geschäftsszenarien mit Marktdynamik

## Pädagogischer Wert

Das Planspiel vermittelt:
- Vollständige GuV-Struktur nach deutschem Handelsrecht
- Unterschied zwischen Gewinn und Liquidität
- Auswirkungen betriebswirtschaftlicher Entscheidungen
- Zusammenhang zwischen Preis, Marketing und Nachfrage
- Kapazitätsplanung und Produktionssteuerung
- Finanzmanagement und Investitionsentscheidungen

## Export-Funktion

Die Excel-Export-Funktion bietet:
- Übersichtsblatt mit allen Quartalen
- Detaillierte Quartalsblätter
- Vollständige GuV für jedes Quartal
- Bilanz mit Aktiva und Passiva
- Cashflow-Rechnung
- Formatierte Tabellen mit professionellem Layout

## Browser-Kompatibilität

Getestet und optimiert für:
- Chrome (empfohlen)
- Firefox
- Safari
- Edge

## Lizenz

Entwickelt für akademische Zwecke an der Ostfalia Hochschule für angewandte Wissenschaften.

## Kontakt

Projekt erstellt für das Modul Business Development Engineering, WiSe 2025/26.

---

**Viel Erfolg beim Lernen!**
