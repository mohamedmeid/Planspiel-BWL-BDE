# 🚀 Deployment Guide - Factory Business Simulation

## Übersicht: 3 Kostenlose Hosting-Optionen

---

## ⭐ **Option 1: Render.com** (EMPFOHLEN für Vorlesungen)

### ✅ Vorteile:
- **100% kostenlos** mit Free Tier
- **Sehr einfach** - 5 Minuten Setup
- **Bleibt online** - keine Auto-Löschung
- **Automatisches HTTPS** - sicher
- **GitHub Integration** - automatisches Deployment

### ⚠️ Nachteile:
- Schläft nach 15 Min Inaktivität (30 Sek Aufwachzeit)
- Gut für Vorlesungen, da Studenten gleichzeitig nutzen

### 📋 Schritt-für-Schritt Anleitung:

#### 1. GitHub Repository erstellen
```bash
cd /Users/mohamedeid/Documents/Planspiel_BWL_BDE
git init
git add .
git commit -m "Initial commit - Factory BWL Planspiel"
```

Gehe zu GitHub.com und erstelle ein neues Repository:
- Name: `factory-bwl-planspiel`
- Public oder Private (beides funktioniert)

```bash
git remote add origin https://github.com/IHR-USERNAME/factory-bwl-planspiel.git
git branch -M main
git push -u origin main
```

#### 2. Render.com Account erstellen
1. Gehe zu: https://render.com
2. Klicke auf **"Get Started"**
3. Registriere dich mit GitHub Account (empfohlen)

#### 3. Web Service erstellen
1. Dashboard → **"New +"** → **"Web Service"**
2. **"Connect a repository"** → Wähle dein `factory-bwl-planspiel` Repo
3. Konfiguration:
   - **Name**: `factory-bwl-planspiel`
   - **Region**: Frankfurt (EU-Central)
   - **Branch**: `main`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: **Free**

4. Klicke auf **"Create Web Service"**

#### 4. Deployment abwarten
- Render baut automatisch die App (3-5 Minuten)
- Status wird angezeigt: Building → Live
- URL wird generiert: `https://factory-bwl-planspiel.onrender.com`

#### 5. Fertig! 🎉
Teile die URL mit deinen Studierenden:
```
https://factory-bwl-planspiel.onrender.com
```

### 💡 Pro-Tipps:
- **Automatisches Deployment**: Jedes `git push` updated die App automatisch
- **Logs ansehen**: Dashboard → Logs (für Debugging)
- **Domain ändern**: Settings → Custom Domains (optional)

---

## 🆓 **Option 2: Railway.app**

### ✅ Vorteile:
- **$5 kostenlos** pro Monat (ausreichend für kleine Apps)
- **Schläft NICHT** (immer online)
- **Sehr schnell** - gute Performance
- **Einfaches Setup**

### ⚠️ Nachteile:
- Nach Verbrauch der $5 muss man bezahlen oder App schläft
- Für kleine Vorlesungen (< 50 Nutzer gleichzeitig) OK

### 📋 Setup:
1. Gehe zu: https://railway.app
2. Sign up mit GitHub
3. **"New Project"** → **"Deploy from GitHub repo"**
4. Wähle dein Repository
5. Railway erkennt automatisch Python
6. **Deploy** - fertig!

URL wird generiert: `https://factory-bwl-planspiel.up.railway.app`

---

## 🐍 **Option 3: PythonAnywhere**

### ✅ Vorteile:
- **100% kostenlos** dauerhaft
- **Bleibt online** ohne zu schlafen
- **Einfach für Python-Apps**
- **Lange Tradition** - sehr stabil

### ⚠️ Nachteile:
- Etwas komplizierter Setup
- Langsamere Performance
- Manuelles Deployment (kein Auto-Deploy)

### 📋 Setup:
1. Gehe zu: https://www.pythonanywhere.com
2. **"Start running Python online in less than a minute!"**
3. Erstelle einen **Free Account**
4. Dashboard → **"Web"** → **"Add a new web app"**
5. Python 3.10, Flask Framework
6. Im Bash Console:
```bash
cd mysite
git clone https://github.com/IHR-USERNAME/factory-bwl-planspiel.git
cd factory-bwl-planspiel
pip install -r requirements.txt
```
7. Web Tab → WSGI Configuration → Code anpassen
8. **Reload** - fertig!

URL: `https://IHR-USERNAME.pythonanywhere.com`

---

## 🏆 **Vergleichstabelle**

| Feature | Render.com | Railway.app | PythonAnywhere |
|---------|-----------|-------------|----------------|
| **Preis** | Kostenlos | $5/Monat gratis | Kostenlos |
| **Schläft?** | Ja (15 Min) | Nein | Nein |
| **Setup-Zeit** | 5 Min | 5 Min | 15 Min |
| **Auto-Deploy** | ✅ | ✅ | ❌ |
| **Performance** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Langlebig** | ✅ | ⚠️ ($5 limit) | ✅ |

---

## 🎓 **Empfehlung für Vorlesungen:**

### **Beste Wahl: Render.com**

**Warum?**
1. ✅ Völlig kostenlos
2. ✅ Bleibt so lange online wie Sie wollen
3. ✅ Einfachstes Setup (5 Minuten)
4. ✅ Automatisches Deployment bei Code-Änderungen
5. ⚠️ Schläft nur bei Inaktivität - **ABER** in Vorlesungen werden Studenten die App gleichzeitig nutzen, daher bleibt sie aktiv!

**Für große Vorlesungen (>50 Studenten):**
- Railway.app (falls Budget vorhanden)
- Oder: Render.com + UptimeRobot (siehe unten)

---

## 💪 **Render.com am Leben erhalten (24/7)**

Falls Sie wollen, dass die App NIEMALS schläft:

### UptimeRobot (Kostenlos):
1. Gehe zu: https://uptimerobot.com
2. Erstelle kostenlosen Account
3. **"Add New Monitor"**
   - Type: HTTP(s)
   - URL: `https://factory-bwl-planspiel.onrender.com`
   - Interval: 5 Minuten
4. UptimeRobot pingt die App alle 5 Min an → bleibt wach!

---

## 🔧 **Troubleshooting**

### Problem: "Application failed to start"
**Lösung**: Prüfe die Logs in Render Dashboard
- Häufig: Fehlende Dependencies in `requirements.txt`

### Problem: "ModuleNotFoundError"
**Lösung**: Füge fehlende Pakete zu `requirements.txt` hinzu

### Problem: "Port already in use"
**Lösung**: Ist nur lokal ein Problem, online kein Issue

---

## 📞 **Support**

Bei Fragen:
- **Render Docs**: https://render.com/docs
- **Railway Docs**: https://docs.railway.app
- **PythonAnywhere Help**: https://help.pythonanywhere.com

---

## ✅ **Nach dem Deployment**

1. **Teste die App** gründlich online
2. **Teile die URL** mit Studierenden
3. **Optional**: Kaufe eine Custom Domain (z.B. `planspiel-factory.de`)
4. **Monitor**: Nutze UptimeRobot für Verfügbarkeits-Überwachung

**Die App ist jetzt live und bereit für die Vorlesung!** 🎉
