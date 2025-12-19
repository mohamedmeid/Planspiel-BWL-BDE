# Spielablauf - Logik

## Überblick
Das Planspiel simuliert **4 Quartale** (1 Geschäftsjahr) einer Produktionsfirma. Jedes Quartal folgt derselben Ablauflogik.

---

## 1. Startzustand (Quartal 1)

| Position | Wert |
|----------|------|
| Liquidität | 28,0 Mio. € |
| Forderungen | 26,0 Mio. € |
| Rohmaterial | 2 Lose |
| Halbfabrikate (WIP) | 2 Lose |
| Fertigwaren | 2 Lose |

---

## 2. Ablauf pro Quartal

### Phase 1: Entscheidungseingabe
Spieler gibt pro Quartal folgende Parameter ein:

- **Verkaufspreis** (€/Los): Standardwert 13,0 Mio.
- **Marketingbudget** (Mio. €): Standardwert 0,0
- **Produktionsmenge** (Lose): Standardwert 2
- **Materialeinkauf** (Lose): Standardwert 2

### Phase 2: Nachfrageberechnung
```
NACHFRAGE = Marktbasis × Preis-Effekt × Marketing-Effekt × Wettbewerbs-Effekt
```

**Formel-Komponenten:**
- **Marktbasis**: 2 Lose pro Quartal
- **Preis-Effekt**: `1,0 - (Preisverhältnis - 1,0) × 0,15`
  - Preisverhältnis = Verkaufspreis / 13,0 Mio.
  - Elastizität: 0,15 (15%)
- **Marketing-Effekt**: `1,0 + (Marketingbudget × 0,08)`
  - Effektivität: 8% pro 1 Mio. €
- **Wettbewerbs-Effekt**:
  - Preis > 12,5 Mio. → Faktor 0,85 (Nachfrageverlust)
  - Preis < 12,5 Mio. → Faktor 1,15 (Nachfragegewinn)
  - Preis = 12,5 Mio. → Faktor 1,0 (neutral)

**Verkaufsmenge**: `min(Nachfrage, Fertigwaren_Lagerbestand)`

### Phase 3: Kostenberechnung

**Variable Kosten:**
```
Materialkosten = Einkaufsmenge × 3,0 Mio. × Marktfaktor
Fertigungskosten = Produktionsmenge × 3,0 Mio.
Montagekosten = Produktionsmenge × 1,0 Mio.
Herstellungskosten = Material + Fertigung + Montage
```

**Fixe und semi-fixe Kosten:**
```
Gemeinkosten = 6,0 Mio. × Gemeinkostenfaktor
Marketingkosten = Eingegebenes Budget
Abschreibungen = 2,25 Mio. (fest, keine Liquiditätswirkung)
Zinsen = 2,5 Mio. (fest, liquiditätswirksam)
```

**Steuern:**
```
Steuern = max(0, Gewinn_vor_Steuern × 0,3333)
```
Nur bei positivem Gewinn

### Phase 4: GuV-Berechnung (Gewinn- und Verlustrechnung)

```
Umsatzerlöse (Revenue)
    = Verkaufsmenge × Verkaufspreis

- Herstellungskosten
= Bruttoergebnis (Gross Profit)

- Gemeinkosten
- Marketingkosten
- Abschreibungen
= Betriebsergebnis / EBIT

- Zinsen
= Gewinn vor Steuern (EBT)

- Steuern
= Gewinn nach Steuern (Jahresüberschuss)
```

### Phase 5: Lagerbestandsaktualisierung

```
Rohmaterial:
    + Materialeinkauf
    - Produktionsmenge

Halbfabrikate (WIP):
    + Produktionsmenge
    - Produktionsmenge (sofort weitergeleitet)

Fertigwaren:
    + Produktionsmenge
    - Verkaufsmenge
```

### Phase 6: Liquiditätsrechnung

```
Liquidität Anfang
    + Zahlungseingang (Forderungen aus Vorquartal)
    - Liquiditätswirksame Kosten:
        • Materialkosten
        • Fertigungskosten
        • Montagekosten
        • Gemeinkosten
        • Marketingkosten
        • Zinsen
        • Steuern
    [NICHT: Abschreibungen - keine Liquiditätswirkung]
= Liquidität Ende

Forderungen neu = Umsatzerlöse (Zahlung nächstes Quartal)
```

**Wichtig:**
- Forderungen aus Q1 werden in Q2 bezahlt
- Forderungen aus Q4 bleiben am Jahresende offen
- Abschreibungen (2,25 Mio.) reduzieren Gewinn, aber nicht Liquidität

### Phase 7: Quartalsergebnis speichern

Alle berechneten Werte werden als Quartalsergebnis gespeichert und dem Spieler angezeigt.

---

## 3. Jahresabschluss (nach Q4)

Nach dem 4. Quartal werden zusammengefasst:

**Summen:**
- Gesamtumsatz (4 Quartale)
- Gesamtkosten (alle Kategorien)
- Gesamtgewinn/-verlust
- Gesamtsteuern

**Kennzahlen:**
- Durchschnittlicher Gewinn pro Quartal
- Umsatzrendite (ROS) = `(Jahresüberschuss / Gesamtumsatz) × 100`
- Endliquidität
- Endbestände aller Lager

---

## 4. Berechnungsreihenfolge (Sequenz)

```
1. Quartalszähler erhöhen
2. Liquidität Anfang speichern
3. Nachfrage berechnen
4. Verkaufsmenge festlegen (min: Nachfrage, Lagerbestand)
5. Alle Kosten berechnen
6. Umsatzerlöse berechnen
7. GuV durchrechnen (Bruttogewinn → EBIT → EBT → Jahresüberschuss)
8. Lagerbestände aktualisieren
9. Liquidität berechnen:
   - Forderungen des Vorquartals kassieren
   - Alle liquiditätswirksamen Kosten abziehen
   - Neue Forderungen erstellen
10. Jahreswerte akkumulieren
11. Quartalsergebnis zurückgeben
```

---

## 5. Wichtige Spielregeln

### Nachfrage
- Minimum: 1 Los (auch im schlechtesten Fall)
- Maximum: Beschränkt durch Fertigwarenlager
- Preiselastizität: 15% (1% Preiserhöhung → 0,15% Nachfragerückgang)
- Wettbewerbseffekt: ±15% je nach relativer Preispositionierung

### Lager
- Rohmaterial: Einkauf erhöht, Produktion verbraucht
- Halbfabrikate: Durchlauf (produziert → sofort montiert)
- Fertigwaren: Produktion erhöht, Verkauf verbraucht
- **Verkaufslimit**: Nicht mehr verkaufbar als Lagerbestand

### Finanzen
- Liquidität kann negativ werden (impliziert Kreditnutzung)
- Fixkosten entstehen unabhängig von Produktion (Gemeinkosten 6 Mio., Abschreibungen 2,25 Mio.)
- Steuern nur bei positivem Gewinn

### Kostenarten
- **Variable Kosten**: Material, Fertigung, Montage (mengenabhängig)
- **Semi-fixe Kosten**: Gemeinkosten (6 Mio.), Marketing (variabel), Zinsen (2,5 Mio. fix)
- **Fixe nicht-liquiditätswirksame Kosten**: Abschreibungen (2,25 Mio.)

---

## 6. Mathematische Formeln im Detail

### Nachfrageformel
```
Preis_Effekt = 1,0 - (Verkaufspreis/13,0 - 1,0) × 0,15

Marketing_Effekt = 1,0 + (Marketingbudget × 0,08)

Wettbewerb_Effekt:
    wenn Verkaufspreis > 12,5: 0,85
    wenn Verkaufspreis < 12,5: 1,15
    sonst: 1,0

Nachfrage = 2 × Preis_Effekt × Marketing_Effekt × Wettbewerb_Effekt
Nachfrage = max(1, Nachfrage)  // Minimum 1 Los

Verkaufsmenge = min(Nachfrage, Fertigwaren_Lagerbestand)
```

### Kostenformeln
```
Materialkosten = Einkaufsmenge × 3,0 × Marktfaktor

Fertigungskosten = Produktionsmenge × 3,0 × Effizienz × Qualität

Montagekosten = Produktionsmenge × 1,0

Herstellungskosten = Materialkosten + Fertigungskosten + Montagekosten
                   = Produktionsmenge × 7,0 (bei Standardwerten)

Gemeinkosten = 6,0 × Gemeinkostenfaktor

Abschreibungen = 2,25 (fest)

Zinsen = 2,5 (fest)
```

### GuV-Formeln
```
Umsatzerlöse = Verkaufsmenge × Verkaufspreis

Bruttoergebnis = Umsatzerlöse - Herstellungskosten

EBIT = Bruttoergebnis - Gemeinkosten - Marketingkosten - Abschreibungen

Gewinn_vor_Steuern = EBIT - Zinsen

Steuern = max(0, Gewinn_vor_Steuern × 0,3333)

Jahresüberschuss = Gewinn_vor_Steuern - Steuern
```

### Liquiditätsformel
```
Zahlungseingang = Forderungen_Vorquartal

Zahlungsausgang = Materialkosten
                + Fertigungskosten
                + Montagekosten
                + Gemeinkosten
                + Marketingkosten
                + Zinsen
                + Steuern

Liquidität_Ende = Liquidität_Anfang + Zahlungseingang - Zahlungsausgang

Forderungen_neu = Umsatzerlöse
```

---

## 7. Lernziele der Spiellogik

1. **Liquidität vs. Gewinn**: Abschreibungen zeigen den Unterschied zwischen buchhalterischem Gewinn und Cashflow
2. **Working Capital Management**: Forderungsverzögerung (1 Quartal) erfordert Liquiditätsplanung
3. **Fixkosten-Falle**: Selbst ohne Produktion fallen 10,75 Mio. € an (Gemeinkosten + Abschreibungen + Zinsen)
4. **Preis-Absatz-Funktion**: Trade-off zwischen Preis und Menge
5. **Marketing-ROI**: 1 Mio. € Marketing → 8% Nachfragesteigerung
6. **Wettbewerbsdruck**: Relative Preispositionierung beeinflusst Marktanteil

---

## 8. Entscheidungsparameter - Wertebereiche

| Parameter | Minimum | Maximum | Standard | Einheit |
|-----------|---------|---------|----------|---------|
| Verkaufspreis | 1,0 | 30,0 | 13,0 | Mio. € |
| Marketing | 0,0 | 10,0 | 0,0 | Mio. € |
| Produktion | 0 | 10 | 2 | Lose |
| Materialeinkauf | 0 | 10 | 2 | Lose |
| Marktfaktor | 0,8 | 1,2 | 1,0 | Faktor |
| Gemeinkostenfaktor | 0,8 | 1,2 | 1,0 | Faktor |

---

## 9. Kritische Erfolgsfaktoren

**Für positiven Cashflow:**
- Verkaufsmenge hoch halten (Nachfrage generieren)
- Verkaufspreis optimal setzen (nicht zu hoch/niedrig)
- Forderungen im Auge behalten (Working Capital)

**Für hohen Gewinn:**
- Bruttoergebnis maximieren (Umsatz - Herstellungskosten)
- Marketingeffizienz nutzen (8% pro 1 Mio. €)
- Produktionskosten minimieren (nur produzieren was verkauft wird)

**Häufige Fehler:**
- Zu hoher Preis → Nachfrage bricht ein
- Überproduktion → Lagerkosten, gebundene Liquidität
- Zu wenig Marketing → Nachfrage unter Kapazität
- Liquidität ignorieren → Insolvenz trotz Gewinn möglich
