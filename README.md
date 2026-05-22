# Mermaiden

Ein Projekt für die Erstellung und Verwaltung von Mermaid-Diagrammen mit Code-Integration.

## Überblick

Mermaiden ist eine Sammlung von Mermaid-Diagrammen und zugehörigem Code, um komplexe Strukturen und Prozesse visuell darzustellen.

## Beispiel: Flowchart

```mermaid
flowchart TD
    A[Start] --> B{Bedingung?}
    B -->|Ja| C[Aktion 1]
    B -->|Nein| D[Aktion 2]
    C --> E[Ende]
    D --> E
```

## Beispiel: Klassendiagramm

```mermaid
classDiagram
    class Projekt {
        +String name
        +String beschreibung
        +erstellen()
        +bearbeiten()
        +löschen()
    }
    
    class Diagramm {
        +String typ
        +String inhalt
        +render()
    }
    
    Projekt "1" --> "*" Diagramm
```

## Installation

```bash
# Klonen Sie dieses Repository
git clone https://github.com/Hoinkkoma/mermaiden-.git
cd mermaiden-
```

## Verwendung

Die Mermaid-Diagramme können direkt in GitHub Markdown-Dateien angezeigt werden.

Für weitere Informationen siehe die [Mermaid-Dokumentation](https://mermaid.js.org/).

## Lizenz

Dieses Projekt ist unter der GPL-3.0 Lizenz lizenziert. Siehe [LICENSE](LICENSE) für Details.

## Autor

[Hoinkkoma](https://github.com/Hoinkkoma)