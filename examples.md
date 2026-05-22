# Mermaid Diagramm Beispiele

## 1. Sequenzdiagramm

```mermaid
sequenceDiagram
    participant Benutzer
    participant System
    participant Datenbank
    
    Benutzer->>System: Anfrage senden
    System->>Datenbank: Daten abrufen
    Datenbank-->>System: Daten zurückgeben
    System-->>Benutzer: Antwort senden
```

## 2. Gantt-Diagramm

```mermaid
gantt
    title Projektplan
    dateFormat YYYY-MM-DD
    
    section Phase
    Planung           :p1, 2026-05-22, 7d
    Entwicklung       :p2, after p1, 14d
    Testing           :p3, after p2, 7d
    Veröffentlichung  :p4, after p3, 3d
```

## 3. Entity-Relationship Diagramm

```mermaid
erDiagram
    PROJEKT ||--o{ DIAGRAMM : enthält
    PROJEKT ||--o{ BENUTZER : gehört_zu
    DIAGRAMM ||--o{ KOMPONENTE : besteht_aus
    
    PROJEKT {
        int id PK
        string name
        string beschreibung
    }
    
    DIAGRAMM {
        int id PK
        int projekt_id FK
        string typ
        string inhalt
    }
    
    BENUTZER {
        int id PK
        string name
        string email
    }
    
    KOMPONENTE {
        int id PK
        int diagramm_id FK
        string name
    }
```

## 4. State Diagramm

```mermaid
stateDiagram-v2
    [*] --> Entwurf
    Entwurf --> Überprüfung: Review starten
    Überprüfung --> Überprüfung: Änderungen anfordern
    Überprüfung --> Genehmigt: Genehmigen
    Genehmigt --> Veröffentlicht: Veröffentlichen
    Veröffentlicht --> [*]
```

## 5. Pie Chart

```mermaid
pie title Zeitverteilung Projekt
    "Planung" : 15
    "Entwicklung" : 50
    "Testing" : 20
    "Dokumentation" : 15
```

## 6. Flowchart Komplexes Beispiel

```mermaid
flowchart TD
    A[Start] --> B{Datenverfügbar?}
    B -->|Ja| C[Daten laden]
    B -->|Nein| D[Fehler: Daten nicht gefunden]
    C --> E{Validierung erfolgreich?}
    E -->|Ja| F[Diagramm generieren]
    E -->|Nein| G[Validierungsfehler]
    F --> H[Export]
    H --> I[Ende]
    D --> I
    G --> I
```

## 7. Klassen-Diagramm

```mermaid
classDiagram
    class MermaidProject {
        -String name
        -List diagrams
        +add_diagram()
        +remove_diagram()
        +export_to_markdown()
    }
    
    class MermaidDiagram {
        -String name
        -String type
        -String content
        +get_markdown()
        +get_html()
        +validate()
    }
    
    MermaidProject "1" --> "*" MermaidDiagram
```