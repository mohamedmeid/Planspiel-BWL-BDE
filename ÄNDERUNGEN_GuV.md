# 🔄 WICHTIGE ÄNDERUNGEN - Abschreibungen, Zinsen und Steuern

## ✅ Was wurde hinzugefügt?

Basierend auf dem Original Factory-Planspiel-Dokument wurden folgende Elemente zur GuV (Gewinn- und Verlustrechnung) hinzugefügt:

### 1. **Abschreibungen (Depreciation)** 💰
- **Pro Quartal:** 2,25 M
- **Pro Jahr:** 9 M (Gebäude 1M + Maschinen 5M + BGA 3M)
- **WICHTIG:** Keine Auswirkung auf Kasse! (nur buchhalterisch)
- **Farbe im Excel:** Orange

### 2. **Zinsen (Interest)** 💳
- **Pro Quartal:** 2,5 M  
- **Pro Jahr:** 10 M (10% von 100M Kredit)
- **Auswirkung:** Reduziert die Kasse
- **Farbe im Excel:** Rot

### 3. **Steuern (Taxes)** 📊
- **Steuersatz:** 33,33% (1/3 des Gewinns vor Steuern)
- **Berechnung:** Nur wenn Gewinn vor Steuern > 0
- **Auswirkung:** Reduziert die Kasse
- **Farbe im Excel:** Rot

---

## 📋 Neue GuV-Struktur (wie im Original)

```
Umsatzerlöse                           99 M
- Herstellungskosten                   56 M
  ├─ Material
  ├─ Fertigung
  └─ Montage
= BRUTTOERGEBNIS                       43 M

- Gemeinkosten                         24 M
- Abschreibungen                        9 M  ← NEU
= BETRIEBSERGEBNIS (EBIT)              10 M

- Zinsen                               10 M  ← NEU
= GEWINN VOR STEUERN                    0 M

- Steuern (33,33%)                      0 M  ← NEU
= GEWINN NACH STEUERN                   0 M
```

---

## 🔍 Detaillierte Erklärung

### Abschreibungen (9 M/Jahr = 2,25 M/Quartal)
**Definition:** Buchhalterische Erfassung der Wertminderung von Anlagevermögen

**Komponenten:**
- Gebäude: 1 M/Jahr = 0,25 M/Quartal
- Maschinen: 5 M/Jahr = 1,25 M/Quartal  
- Betriebs- und Geschäftsausstattung: 3 M/Jahr = 0,75 M/Quartal

**Wichtig:**
- ❌ KEIN Geld fließt aus der Kasse!
- ✅ Reduziert nur den buchhalterischen Gewinn
- ℹ️ "Der Wert eines Vermögensgegenstandes sinkt, aber es fließt KEIN Geld aus der Kasse!"

### Zinsen (10 M/Jahr = 2,5 M/Quartal)
**Definition:** Finanzierungskosten für Kredite

**Berechnung:**
- Kreditvolumen: 100 M
- Zinssatz: 10% p.a.
- Jährliche Zinsen: 100 M × 10% = 10 M
- Quartalsweise: 10 M ÷ 4 = 2,5 M

**Wichtig:**
- ✅ Geld fließt aus der Kasse!
- ✅ Reduziert Liquidität

### Steuern (33,33% des Gewinns vor Steuern)
**Definition:** Körperschaftssteuer auf Unternehmensgewinne

**Berechnung:**
```python
if gewinn_vor_steuern > 0:
    steuern = gewinn_vor_steuern × 0,3333
else:
    steuern = 0
```

**Wichtig:**
- ✅ Geld fließt aus der Kasse!
- ✅ Nur bei positivem Gewinn
- ✅ Reduziert Liquidität

---

## 📊 Beispiel-Berechnung

### Quartal mit Gewinn:

```
Umsatzerlöse:                    26,00 M
- Herstellungskosten:            14,00 M
= Bruttoergebnis:                12,00 M

- Gemeinkosten:                   6,00 M
- Marketing:                      1,00 M
- Abschreibungen:                 2,25 M
= EBIT:                           2,75 M

- Zinsen:                         2,50 M
= Gewinn vor Steuern:             0,25 M

- Steuern (33,33%):               0,08 M
= GEWINN NACH STEUERN:            0,17 M
```

### Cash Flow:
```
Kasse Anfang:                    28,00 M
+ Einzahlungen (Forderungen):    26,00 M
- Material:                       6,00 M
- Fertigung:                      6,00 M
- Montage:                        2,00 M
- Gemeinkosten:                   6,00 M
- Marketing:                      1,00 M
- Zinsen:                         2,50 M  ← Cash-wirksam
- Steuern:                        0,08 M  ← Cash-wirksam
+ Abschreibungen:                 0,00 M  ← NICHT cash-wirksam!
= Kasse Ende:                    30,42 M
```

---

## 💻 Code-Änderungen

### Neue Felder in `QuarterResult`:
```python
herstellungskosten: float      # Gesamt (Material+Produktion+Montage)
depreciation: float            # Abschreibungen - NICHT cash-wirksam
interest: float                # Zinsen - cash-wirksam
gross_profit: float            # Bruttoergebnis
ebit: float                    # Betriebsergebnis
profit_before_tax: float       # Gewinn vor Steuern
tax: float                     # Steuern - cash-wirksam
net_profit: float              # Gewinn nach Steuern
```

### Neue Parameter in `GameParameters`:
```python
depreciation_per_quarter: float = 2.25   # 9M/Jahr ÷ 4
interest_per_quarter: float = 2.5        # 10M/Jahr ÷ 4
tax_rate: float = 0.3333                 # 33,33%
credit_volume: float = 100.0             # Kredit
interest_rate: float = 0.10              # 10%
```

---

## 📈 Neue Ausgaben

### Konsole (Python):
```
QUARTAL 1 - GEWINN- UND VERLUSTRECHNUNG

Umsatzerlöse:                   26.00 M
  (Verkaufspreis: 13.00 M × 2 Lose)

Herstellungskosten:             14.00 M
  Material:                      6.00 M
  Fertigung:                     6.00 M
  Montage:                       2.00 M

= Bruttoergebnis:               12.00 M

Gemeinkosten:                    6.00 M
Marketing:                       1.00 M
Abschreibungen:                  2.25 M

= Betriebsergebnis (EBIT):       2.75 M

Zinsen:                          2.50 M

= Gewinn vor Steuern:            0.25 M

Steuern (33.33%):                0.08 M

= GEWINN NACH STEUERN:           0.17 M
```

### Excel Export:
Die Excel-Datei zeigt jetzt:
- ✅ Vollständige GuV wie im Original
- ✅ Abschreibungen pro Quartal und Jahr
- ✅ Zinsen pro Quartal und Jahr
- ✅ Steuern pro Quartal und Jahr
- ✅ Farbcodierung (Orange für Abschreibungen, Rot für Zinsen/Steuern)

---

## 🎯 Wichtige Unterschiede zum vorherigen Code

### ALT (ohne Abschreibungen/Zinsen/Steuern):
```
Umsatz - Alle Kosten = Nettogewinn
```

### NEU (mit Abschreibungen/Zinsen/Steuern):
```
Umsatz 
- Herstellungskosten 
= Bruttoergebnis
- Gemeinkosten
- Abschreibungen (nicht cash-wirksam)
= EBIT
- Zinsen (cash-wirksam)
= Gewinn vor Steuern
- Steuern (cash-wirksam)
= Gewinn nach Steuern
```

---

## ✅ Checkliste - Was funktioniert jetzt?

- [x] Abschreibungen werden berechnet (2,25 M/Quartal)
- [x] Zinsen werden berechnet und von Kasse abgezogen (2,5 M/Quartal)
- [x] Steuern werden berechnet und von Kasse abgezogen (33,33% bei Gewinn)
- [x] GuV-Struktur entspricht Original Factory-Dokument
- [x] Jahresabschluss zeigt totale Abschreibungen (9 M)
- [x] Jahresabschluss zeigt totale Zinsen (10 M)
- [x] Jahresabschluss zeigt totale Steuern
- [x] Cash Flow berücksichtigt nur cash-wirksame Posten
- [x] Excel-Export mit vollständiger GuV-Struktur
- [x] Farbcodierung in Excel

---

## 🚀 So testen Sie die Änderungen

### 1. Python Kommandozeile:
```bash
cd ~/Documents/Planspiel_BWL_BDE
python3 factory_simulator.py
```

Achten Sie auf die neue GuV-Struktur in der Ausgabe!

### 2. Web-Interface:
```bash
cd ~/Documents/Planspiel_BWL_BDE
python3 app.py
```

Die Ergebnisse zeigen jetzt:
- Bruttoergebnis
- EBIT
- Gewinn vor Steuern
- Steuern
- Gewinn nach Steuern

### 3. Excel-Export:
Nach dem Spielen können Sie die Ergebnisse als Excel exportieren.
Die Excel-Datei zeigt die vollständige GuV wie im Original!

---

## 📝 Für Ihre Präsentation

### Erklären Sie:

1. **Warum Abschreibungen?**
   - Erfassen Wertminderung von Anlagevermögen
   - Keine Cash-Auswirkung
   - 9 M/Jahr (Gebäude 1M, Maschinen 5M, BGA 3M)

2. **Warum Zinsen?**
   - Finanzierungskosten für 100M Kredit
   - 10% Zinssatz = 10 M/Jahr
   - Cash-Auswirkung!

3. **Warum Steuern?**
   - Körperschaftssteuer auf Gewinne
   - 33,33% (1/3) des Gewinns vor Steuern
   - Cash-Auswirkung!

4. **GuV-Struktur:**
   - Entspricht Original Factory-Spiel
   - Zeigt operative Performance (EBIT)
   - Zeigt finanzielle Performance (nach Zinsen)
   - Zeigt Netto-Performance (nach Steuern)

---

## 🎓 Lernziele erreicht

✅ **Verständnis der GuV-Struktur**
- Umsatzerlöse → Bruttoergebnis → EBIT → Gewinn nach Steuern

✅ **Unterscheidung cash-wirksam vs. nicht cash-wirksam**
- Abschreibungen: nur buchhalterisch
- Zinsen & Steuern: reduzieren Kasse

✅ **Realistische Unternehmensrechnung**
- Wie im Original Factory-Planspiel
- Wie in echten Unternehmen

---

**Datum:** November 2025  
**Version:** 2.0 (mit Abschreibungen, Zinsen, Steuern)  
**Status:** ✅ Vollständig implementiert und getestet
