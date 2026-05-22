#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Mermaid Diagramm Converter
Ein Utility zur Konvertierung und Verwaltung von Mermaid-Diagrammen
"""

class MermaidDiagram:
    """Klasse zur Verwaltung von Mermaid-Diagrammen"""
    
    def __init__(self, name, diagram_type, content):
        """
        Initialisiert ein neues Mermaid-Diagramm
        
        Args:
            name (str): Name des Diagramms
            diagram_type (str): Typ des Diagramms (flowchart, sequence, etc.)
            content (str): Der Mermaid-Code des Diagramms
        """
        self.name = name
        self.diagram_type = diagram_type
        self.content = content
    
    def get_markdown(self):
        """
        Gibt das Diagramm als Markdown-Code-Block zurück
        
        Returns:
            str: Das Diagramm formatiert als Markdown
        """
        return f"""```mermaid
{self.content}
```"""
    
    def get_html(self):
        """
        Gibt das Diagramm als HTML-Code zurück
        
        Returns:
            str: Das Diagramm mit Mermaid.js HTML-Tag
        """
        return f"""<div class="mermaid">
{self.content}
</div>"""
    
    def validate(self):
        """
        Validiert den Mermaid-Code
        
        Returns:
            bool: True wenn valide, False sonst
        """
        if not self.content or not self.diagram_type:
            return False
        return True
    
    def __str__(self):
        return f"MermaidDiagram(name={self.name}, type={self.diagram_type})"


class MermaidProject:
    """Klasse zur Verwaltung eines Mermaid-Projekts"""
    
    def __init__(self, project_name):
        """Initialisiert ein neues Projekt"""
        self.project_name = project_name
        self.diagrams = []
    
    def add_diagram(self, diagram):
        """Fügt ein Diagramm zum Projekt hinzu"""
        self.diagrams.append(diagram)
        return True
    
    def remove_diagram(self, name):
        """Entfernt ein Diagramm aus dem Projekt"""
        self.diagrams = [d for d in self.diagrams if d.name != name]
    
    def get_all_diagrams(self):
        """Gibt alle Diagramme zurück"""
        return self.diagrams
    
    def count_diagrams(self):
        """Zählt die Diagramme im Projekt"""
        return len(self.diagrams)
    
    def export_to_markdown(self):
        """
        Exportiert alle Diagramme als Markdown
        
        Returns:
            str: Alle Diagramme als formatierter Markdown
        """
        output = f"# {self.project_name}\n\n"
        for diagram in self.diagrams:
            output += f"## {diagram.name}\n\n"
            output += diagram.get_markdown()
            output += "\n\n"
        return output


# Beispiele
if __name__ == "__main__":
    # Erstelle ein neues Projekt
    project = MermaidProject("Mein Mermaid Projekt")
    
    # Erstelle einige Diagramme
    flowchart = MermaidDiagram(
        "Einfaches Flowchart",
        "flowchart",
        """flowchart TD
    A[Start] --> B[Verarbeitung]
    B --> C[Ende]"""
    )
    
    sequence = MermaidDiagram(
        "Sequenzdiagramm",
        "sequence",
        """sequenceDiagram
    participant A as Akteur A
    participant B as Akteur B
    A->>B: Nachricht
    B-->>A: Antwort"""
    )
    
    # Füge sie zum Projekt hinzu
    project.add_diagram(flowchart)
    project.add_diagram(sequence)
    
    # Gib Informationen aus
    print(f"Projekt: {project.project_name}")
    print(f"Anzahl Diagramme: {project.count_diagrams()}")
    print("\nDiagramme:")
    for d in project.get_all_diagrams():
        print(f"  - {d}")
    
    # Exportiere zu Markdown
    print("\n" + "="*50)
    print(project.export_to_markdown())