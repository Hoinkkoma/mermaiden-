
# 🤖 Automation Dokumentation für Mermaiden

## 📌 Überblick

Dieses Projekt ist vollständig konfiguriert für automatische Updates, Tests und Validierung durch GitHub Actions.

---

## 📋 Verfügbare Workflows

### 1️⃣ Auto-Update Workflow (`auto-update.yml`)

**Zeitplan:** Täglich um 09:00 UTC  
**Trigger:** `schedule: cron: '0 9 * * *'`

#### Was es macht:
- ✅ Validiert Python-Code Syntax
- 🔄 Aktualisiert Timestamp im README
- 💾 Committed und pusht Änderungen automatisch
- 📊 Überwacht Code-Qualität
- 🔐 Verwendet automatische `GITHUB_TOKEN`

**Log:** [Action Logs](https://github.com/Hoinkkoma/mermaiden-/actions)

---

### 2️⃣ Test Workflow (`tests.yml`)

**Trigger:** Bei jedem Push und Pull Request

#### Was es macht:
- ✅ Syntax-Validierung des Python-Codes
- 🧪 Führt Unit-Tests durch
- ✔️ Validiert `MermaidDiagram` Klasse
- ✔️ Validiert `MermaidProject` Klasse
- 🐍 Testet mit Python 3.9+

---

## 🔧 Manuelle Workflow-Trigger

### Über GitHub CLI

```bash
# Auto-Update manuell ausführen
gh workflow run auto-update.yml

# Tests manuell ausführen
gh workflow run tests.yml
```

### Über Web-UI

1. Gehen Sie zu **Actions** Tab
2. Wählen Sie den gewünschten Workflow
3. Klicken Sie "Run workflow"
4. Bestätigen Sie mit "Run workflow"

---

## 📊 Status Badges

Kopiere diese Badges in dein README:

```markdown
![Auto-Update](https://github.com/Hoinkkoma/mermaiden-/actions/workflows/auto-update.yml/badge.svg)
![Tests](https://github.com/Hoinkkoma/mermaiden-/actions/workflows/tests.yml/badge.svg)
```

Aktuelle Status:
- ![Auto-Update](https://github.com/Hoinkkoma/mermaiden-/actions/workflows/auto-update.yml/badge.svg)
- ![Tests](https://github.com/Hoinkkoma/mermaiden-/actions/workflows/tests.yml/badge.svg)

---

## 📝 Automatische Commits

Commits durch Workflows werden mit 🔄 markiert:

```
🔄 Auto-Update: 2026-05-22 09:00:00 UTC
```

**Eigenschaften:**
- Author: `github-actions[bot]`
- Automatisch gepusht
- Keine manuellen Änderungen nötig

---

## ⚙️ Workflow-Konfiguration

### Zeitplan anpassen

Editieren Sie `.github/workflows/auto-update.yml`:

```yaml
schedule:
  - cron: '0 9 * * *'  # HH MM * * *
```

**Cron Format:** `minute hour day month weekday`

**Beispiele:**
- `0 9 * * *` = 09:00 UTC täglich
- `0 9 * * 1` = 09:00 UTC jeden Montag
- `0 */6 * * *` = Alle 6 Stunden

### Berechtigungen konfigurieren

Workflows nutzen `GITHUB_TOKEN` mit Permissions:

```yaml
permissions:
  contents: write  # Erlaubt Commits
  actions: read    # Liest Workflow-Status
```

---

## 🔍 Logs und Debugging

### Logs anschauen

1. Gehen Sie zu **Actions** Tab
2. Wählen Sie einen Workflow-Run
3. Klicken Sie auf einen Job
4. Sehen Sie die detaillierten Logs

### Häufige Probleme

| Problem | Lösung |
|---------|--------|
| ❌ Workflow läuft nicht | Überprüfen Sie `.github/workflows/` Dateien |
| ❌ Push fehlgeschlagen | Überprüfen Sie Repository Permissions |
| ❌ Tests fehlgeschlagen | Sehen Sie Job-Logs für Details |

---

## 📧 Benachrichtigungen

### Standard-Benachrichtigungen

- ✅ **Erfolgreiche Runs:** Keine Benachrichtigung
- ❌ **Fehlgeschlagene Runs:** GitHub Email-Benachrichtigung
- ⚠️ **Warnungen:** Im Actions-Tab sichtbar

### Benachrichtigungen anpassen

1. Gehen Sie zu **Settings** → **Notifications**
2. Wählen Sie **Actions** Benachrichtigungen
3. Konfigurieren Sie nach Bedarf

---

## 🚀 Best Practices

### ✅ Empfehlungen

- 🔄 Regelmäßige automatische Tests durchführen
- 📊 Status Badges in README verwenden
- 🔐 Niemals `GITHUB_TOKEN` ändern
- 📝 Commit-Messages dokumentieren
- 🧪 Lokal testen vor Push

### ❌ Zu vermeiden

- Direkte Änderungen an Workflow-Secrets
- Zu häufige Schedules (Performance)
- Workflows ohne Fehlerbehandlung
- Fehlende Log-Überprüfung

---

## 📚 Ressourcen

- 📖 [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
- 🔗 [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- ⏰ [Cron Expression Builder](https://crontab.guru/)
- 🧪 [Testing Guide](https://docs.github.com/en/actions/automating-builds-and-tests)

---

## ✨ Zusammenfassung

| Aspekt | Status |
|--------|--------|
| 🤖 Auto-Update | ✅ Aktiv |
| 🧪 Tests | ✅ Aktiv |
| 📊 Monitoring | ✅ Aktiv |
| 🔐 Sicherheit | ✅ Gesichert |
| 📈 Performance | ✅ Optimiert |

**Alles ist konfiguriert und läuft automatisch!** 🎉

---

## 📞 Support

Bei Fragen zu den Workflows:
1. Überprüfen Sie die [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
2. Sehen Sie sich die [Workflow-Logs](https://github.com/Hoinkkoma/mermaiden-/actions) an
3. Erstellen Sie ein [Issue](https://github.com/Hoinkkoma/mermaiden-/issues)

**Viel Erfolg mit deinen Workflows!** 🚀
