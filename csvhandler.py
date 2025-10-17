import csv
from PyQt5.QtWidgets import QTreeWidgetItem

# ladet csv, iteriert über Spalten 0-6 für Thesaurusbaum
def load_csv_into_tree(csv_path, tree_widget):
    tree_widget.clear()
    tree_widget.setColumnCount(1)
    tree_widget.setHeaderLabels(["CSV Thesaurus-Hierarchie"])

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        print("CSV-Spalten:", reader.fieldnames)
        cols = [f"_standard#de-DE#{i}" for i in range(7)] #wenn mehr als 7 Ebenen, hier ändern

        root_items = {}  

        for row in reader:
            parent = None
            for col in cols:
                name = row.get(col, "").strip()
                if not name:
                    break

                if parent is None:
                    if name not in root_items:
                        item = QTreeWidgetItem([name])
                        tree_widget.addTopLevelItem(item)
                        root_items[name] = item
                        print(f"Füge Top-Level Item hinzu: {name}")
                    parent = root_items[name]
                else:
                    child = None
                    for i in range(parent.childCount()):
                        if parent.child(i).text(0) == name:
                            child = parent.child(i)
                            break
                    if child is None:
                        child = QTreeWidgetItem([name])
                        parent.addChild(child)
                        print(f"Füge Kind hinzu: {name} unter {parent.text(0)}")
                    parent = child
