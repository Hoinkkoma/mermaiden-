# Automation Dokumentation für Mermaiden

## 🤖 Automatische Updates

Dieses Projekt ist so konfiguriert, dass es sich automatisch aktualisiert und validiert.

## 📋 Workflows

### 1. Auto-Update Workflow (auto-update.yml)
**Trigger:** Täglich um 09:00 UTC

**Was es macht:**
- ✅ Validiert Python-Code Syntax
- 🔄 Aktualisiert Timestamp im README
- 💾 Committed und pusht Änderungen automatisch
- 📊 Überwacht Code-Qualität

**Logs:** https://github.com/Hoinkkoma/mermaiden-/actions

---

### 2. Test Workflow (tests.yml)
**Trigger:** Bei jedem Push und Pull Request

**Was es macht:**
- ✅ Syntax-Validierung des Python-Codes
- 🧪 Führt Unit-Tests durch
- ✔️ Validiert MermaidDiagram Klasse
- ✔️ Validiert MermaidProject Klasse

---

## 🔧 Manuelle Trigger

Sie können Workflows auch manuell auslösen:

```bash
# Über GitHub CLI
gh workflow run auto-update.yml
```

Oder über die Web-UI:
1. Gehen Sie zum **Actions** Tab
2. Wählen Sie den Workflow
3. Klicken Sie "Run workflow"

---

## 📊 Status Check

Status Badge für README:
```markdown
![Auto-Update](https://github.com/Hoinkkoma/mermaiden-/actions/workflows/auto-update.yml/badge.svg)
![Tests](https://github.com/Hoinkkoma/mermaiden-/actions/workflows/tests.yml/badge.svg)
```

---

## 📝 Commit History

Automatische Commits werden mit 🔄 markiert:
- `🔄 Auto-Update: 2026-05-22 09:00:00 UTC`

---

## ⚙️ Konfiguration

### Zeitplan ändern
Editieren Sie `.github/workflows/auto-update.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'  # 09:00 UTC täglich
```

Cron Format: `minute hour day month weekday`

---

## 🔐 Berechtigungen

Workflows nutzen `GITHUB_TOKEN` mit Permissions:
- `contents: write` - Erlaubt Commits
- `actions: read` - Liest Workflow-Status

---

## 📧 Benachrichtigungen

- ✅ Erfolgreiche Updates: Kein Benachrichtigungen
- ❌ Fehler: GitHub Email-Benachrichtigung

---

## 🚀 Nächste Schritte

1. ✅ Workflows sind aktiv
2. ✅ Tests laufen bei jedem Push
3. ✅ Updates laufen täglich
4. ✅ Code wird automatisch validiert

**Alles funktioniert automatisch!** 🎉
