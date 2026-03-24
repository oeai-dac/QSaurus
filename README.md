# QSaurus

Das Plugin soll die Einbindung von kontrollierten Vokabularien in QGIS erleichtern. Entwickelt wurde es spezifisch für das Österreichische Archäologische Institut, dementsprechend sind diese Thesauri über die Checkboxen aktivierbar. 
Mittels des Plugins können aber alle Thesauri eingebunden werden, sofern sie bestimmte Voraussetzungen erfüllen. 

## Funktionalität:
### Layer und Attributauswahl: 
Es muss ein Layer sowie ein Attributfeld ausgewählt werden, für das die ausgewählten Begriffe übernommen werden
Mit "Begriffe in Attrbuttabelle laden" wird folgendes ausgelöst:
1. der Widget-Type des ausgewählten Attributfeldes wird auf "Value Map" umgestellt
2. die ausgewählten Begriffe werden sowohl als Value wie auch als Description dem Feld hinzugefügt
3. bereits bestehende Begriffe werden dabei nicht verändert oder gelöscht

### Auswahl der zu übernehmenden Begriffe: 
Begriffe können folgendermassen ausgewählt werden:
1. durch Ctrl können einzelne oder mehrere Begriffe separat ausgewählt werden
2. durch Shift können Bereiche zwischen zwei Begriffen ausgewählt werden
3. durch das Aufziehen eines "Fensters" können alle Begriffe im "Fenster" ausgewählt werden

Eine rekursive Auswahl ist momentan nicht möglich, durch "Alle Ebenen ausklappen" und z.B. die Fensterauswahl können aber viele Begriffe einfach übernommen werden

### Suche nach Begriffen im geladenen Thesaurus:
Bei Eingabe einer Zeichenkombination oder eines ganzen Suchbegriffes, wird diese Kombination/dieser Begriff hervorgehoben und alle betroffenen Ebenen ausgeklappt

### Voreingestellte Thesauri: 
1. ÖAI Kulturepochen: https://vocabs.acdh.oeaw.ac.at/oeai-cp/de/
2. ÖAI Materialien: https://vocabs.acdh.oeaw.ac.at/oeai-materials_browse/de/

### Manuelles Einbinden von Thesauri: 
diese müssen in ihrer Form allerdings den Vocabs-Thesauri des ÖAI entsprechen:
1. Dafür kann ein Turtle .ttl über einen Link eingebunden oder als lokale Datei geladen werden. Voraussetzung ist
  1. ein SKOS.prefLabel (Begriffe selbst) 
  2. sowie SKOS.broader (für die Hierarchie)

2. Es kann auch eine lokale .csv Datei in welcher die Hierarchie durch Spalten wiedergegeben wird, geladen werden. Dazu muss die Form folgendermassen sein:
  1. Die Spalten müssen folgendermassen benannt sein "_standard#de-DE#n" wobei n die Werte 0 (für parent) bis 6 haben kann
    > sollten mehr als 7 Ebenen benötigt werden: im Script csvhandler.py die entsprechend kommentierte Zeile ändern (momentan Zeile 13)
  2. Bei Child-Begriffen müssen die entsprechenden parent-Begriffe ebenfalls vorhanden sein

unter ".csv/.ttl Vorlagen" sind Vorlagen gespeichert, welche die genaue Struktur zeigen und dementsprechend genutzt werden könnten

### Laden englischer Begriffe:
Mit aktivierter Option "Optional: Load Englisch Terms of the Thesarus" werden die englischen Begriffe von ÖAI Kulturepochen bzw. ÖAI Materialien geladen

### Layerstil-Datei
Da der Widget-Type und somit auch die zugehörigen bzw. auswählbaren Begriffe in QGIS im Layerstil gespeichert werden, wird jeweils der Stil automatisch in die Geopackage-Datenbank oder als .qml mit allen neuen Begriffen als qsaurus_n (wobei n=Ordnungszahl) gespeichert und kann bei neuen Projekten dazugeladen werden 


-------------------------

#Englisch

The plugin is designed to facilitate the integration of controlled vocabularies into QGIS. It was developed specifically for the Austrian Archaeological Institute, so these thesauri can be enabled via the checkboxes.
However, the plugin can be used to integrate any thesauri, provided they meet certain requirements.  

## Functionalities:
### Layer and Attribute Selection: 
You must select a layer and an attribute field to which the selected terms will be applied
Selecting ‘Load terms into attribute table’ triggers the following:
1. The widget type of the selected attribute field is changed to ‘Value Map’
2. The selected terms are added to the field as both values and descriptions
3. Existing terms are not altered or deleted

### Selecting the Terms to be Imported: 
Terms can be selected as follows:
1. Use Ctrl to select individual terms or multiple terms separately
2. Use Shift to select ranges between two terms
3. Drag to create a ‘selection box’ to select all terms within the box

Recursive selection is not currently possible, but by using ‘Expand all levels’ and, for example, the window selection, many terms can be easily selected

### Search for Terms in the Loaded Thesaurus:
When you enter a combination of characters or a full search term, that combination or term is highlighted and all relevant levels are expanded

### Predefined Thesauri: 
1. ÖAI Cultural Time Periods: https://vocabs.acdh.oeaw.ac.at/oeai-cp/en/
2. ÖAI Materials: https://vocabs.acdh.oeaw.ac.at/oeai-materials_browse/en/

### Manual Integration of Thesauri: 
However, these must conform to the OeAI Vocabs thesauri in terms of format:
1. To do this, a Turtle .ttl file can be embedded via a link or loaded as a local file. The prerequisites are
  1. a SKOS.prefLabel (the terms themselves) 
  2. and a SKOS.broader (for the hierarchy)

2. A local .csv file in which the hierarchy is represented by columns can also be loaded. To do this, the format must be as follows:
  1. The columns must be named as follows: ‘_standard#de-DE#n’, where n can have values from 0 (for parent) to 6
    > If more than 7 levels are required: in the csvhandler.py script, change the relevant commented-out line (currently line 13)
  2. For child terms, the corresponding parent terms must also be present

Templates are stored under “.csv/.ttl Templates”, which show the exact structure and can be used accordingly

### Loading English Terms:
If the option ‘Optional: Load English terms from the thesaurus’ is enabled, the English terms for ÖAI cultural periods and ÖAI materials will be loaded

### Layer Style File
As the widget type and, consequently, the associated or selectable terms are stored in the layer style in QGIS, the style is automatically saved to the geopackage database or as a .qml file containing all new terms under the name qsaurus_n (where n = ordinal number), and can be loaded into new projects 
