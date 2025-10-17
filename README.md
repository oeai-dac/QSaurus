# QSaurus

Das Plugin soll die Einbindung von kontrollierten Vokabularien in QGIS erleichtern. Entwickelt wurde es spezifisch für das Österreichische Archäologische Institut, dementsprechend sind diese Thesauri über die Checkboxen aktivierbar. 
Mittels des Plugins können aber alle Thesauri eingebunden werden, sofern sie bestimmte Voraussetzungen erfüllen. 

## Funktionalität:
- Es muss ein Layer sowie ein Attributfeld ausgewählt werden, für das die ausgewählten Begriffe übernommen werden
- Mit "Begriffe in Attrbuttabelle laden" wird folgendes ausgelöst:
 1. der Widget-Type des ausgewählten Attributfeldes wird auf "Value Map" umgestellt
 2. die ausgewählten Begriffe werden sowohl als Value wie auch als Description dem Feld hinzugefügt
 3. bereits bestehende Begriffe werden dabei nicht verändert oder gelöscht
- Begriffe können folgendermassen ausgewählt werden:
 1. durch Ctrl können einzelne oder mehrere Begriffe separat ausgewählt werden
 2. durch Shift können Bereiche zwischen zwei Begriffen ausgewählt werden
 3. durch das Aufziehen eines "Fensters" können alle Begriffe im "Fenster" ausgewählt werden

Eine rekursive Auswahl ist momentan nicht möglich, durch "Alle Ebenen ausklappen" und z.B. die Fensterauswahl können aber viele Begriffe einfach übernommen werden
- Bei Eingabe einer Zeichenkombination oder eines ganzen Suchbegriffes, wird diese Kombination/dieser Begriff hervorgehoben und alle betroffenen Ebenen ausgeklappt
- Voreingestellte Thesauri:
 1. ÖAI Kulturepochen: https://vocabs.acdh.oeaw.ac.at/oeai-cp/de/
 2. ÖAI Materialien: https://vocabs.acdh.oeaw.ac.at/oeai-materials_browse/de/
- Selbst eingebundene Thesauri; diese müssen in ihrer Form allerdings den Vocabs-Thesauri des ÖAI entsprechen:
 1. Dafür kann ein Turtle .ttl über einen Link eingebunden oder als lokale Datei geladen werden. Voraussetzung ist
  1. ein SKOS.prefLabel (Begriffe selbst) 
  2. sowie SKOS.broader (für die Hierarchie)
 2. Es kann auch eine lokale .csv Datei in welcher die Hierarchie durch Spalten wiedergegeben wird, geladen werden. Dazu muss die Form folgendermassen sein:
  1. Die Spalten müssen folgendermassen benannt sein "_standard#de-DE#n" wobei n die Werte 0 (für parent) bis 6 haben kann
    > sollten mehr als 7 Ebenen benötigt werden: im Script csvhandler.py die entsprechend kommentierte Zeile ändern (momentan Zeile 13)
  2. Bei Child-Begriffen müssen die entsprechenden parent-Begriffe ebenfalls vorhanden sein
  > unter ".csv/.ttl Vorlagen" sind Vorlagen gespeichert, welche die genaue Struktur zeigen und dementsprechend genutzt werden könnten
- Da der Widget-Type und somit auch die zugehörigen bzw. auswählbaren Begriffe in QGIS im Layerstil gespeichert werden, wird jeweils der Stil automatisch in die Geopackage-Datenbank oder als .qml mit allen neuen Begriffen als qsaurus_n (wobei n=Ordnungszahl) gespeichert und kann bei neuen Projekten dazugeladen werden 
- Mit aktivierter Option "Optional: Load Englisch Terms of the Thesarus" werden die englischen Begriffe von ÖAI Kulturepochen bzw. ÖAI Materialien geladen
