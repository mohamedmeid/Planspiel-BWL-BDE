# ⚡ 5-Minuten Deployment zu Render.com

## Schritt 1: GitHub hochladen (2 Min)

```bash
cd /Users/mohamedeid/Documents/Planspiel_BWL_BDE

# Git initialisieren
git init
git add .
git commit -m "Factory BWL Planspiel - Ready for deployment"

# GitHub Repo erstellen auf github.com → "New Repository"
# Name: factory-bwl-planspiel

# Hochladen
git remote add origin https://github.com/IHR-USERNAME/factory-bwl-planspiel.git
git branch -M main
git push -u origin main
```

## Schritt 2: Render.com Deployment (3 Min)

1. **Gehe zu**: https://render.com
2. **Sign up** mit GitHub Account
3. **New +** → **Web Service**
4. **Connect Repository** → Wähle `factory-bwl-planspiel`
5. **Konfiguration**:
   - Name: `factory-bwl-planspiel`
   - Runtime: **Python 3**
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
   - Instance: **Free**
6. **Create Web Service**

## Schritt 3: Fertig! (30 Sek)

Warte bis Status: **Live** (3-5 Min)

Deine URL: `https://factory-bwl-planspiel.onrender.com`

---

## 💡 Bonus: Nie schlafen (Optional)

**UptimeRobot** (kostenlos):
1. https://uptimerobot.com → Sign up
2. Add Monitor → HTTP(s)
3. URL: `https://factory-bwl-planspiel.onrender.com`
4. Interval: 5 Minuten

Fertig! App pingt sich selbst alle 5 Min → bleibt wach 24/7

---

## 🎉 Das war's!

**Teile die URL mit Studierenden und los geht's!**
