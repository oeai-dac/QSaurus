import requests
from rdflib import Graph, Literal
from anytree import Node, RenderTree
from rdflib.namespace import RDF, SKOS
from qgis.core import QgsEditorWidgetSetup


# Extract Prefered labels
def extract_labels(graph):
    labels = []
    for s in graph.subjects(RDF.type, SKOS.Concept):
        label = next(graph.objects(s, SKOS.prefLabel), None)
        if label:
            labels.append(str(label))
    return labels


# Bildet Thesaurusbaum über SKOS.broader
def build_tree(graph, lang_preference=None):
    concepts = {}
    for s in graph.subjects(RDF.type, SKOS.Concept):
        uri = str(s)

        # Sprachpräferenz beachten
        label = None
        if lang_preference:
            for l in graph.objects(s, SKOS.prefLabel):
                if isinstance(l, Literal) and l.language == lang_preference:
                    label = l
                    break
        if label is None:
            label = next(graph.objects(s, SKOS.prefLabel), None)

        broader = next(graph.objects(s, SKOS.broader), None)
        label_str = str(label) if label else uri
        broader_str = str(broader) if broader else None

        concepts[uri] = {
            "label": label_str,
            "broader": broader_str
        }

    nodes = {uri: Node(data["label"]) for uri, data in concepts.items()}
    for uri, data in concepts.items():
        parent = data["broader"]
        if parent and parent in nodes:
            nodes[uri].parent = nodes[parent]
    roots = [n for uri, n in nodes.items() if concepts[uri]["broader"] is None]

    return roots

# Laden der beiden voreingestellten Thesauri (Materialien und Kulturepochen)
def load_graph(kategorie="Kulturepochen"):
    if kategorie == "Materialien":
        print("Materialien ist aktiviert")
        url = "https://vocabs-downloads.acdh.oeaw.ac.at/vocabs-main/Archaeology/OeAIMaterials/oeai_materials.ttl"
    elif kategorie == "Kulturepochen":
        print("Kulturepochen ist aktiviert")
        url = "https://vocabs-downloads.acdh.oeaw.ac.at/vocabs-main/Archaeology/OeAICulturalTimePeriods/oeai_cultural_time_periods.ttl"
    else:
        print("Unbekannte Kategorie:", kategorie)
        return None

    headers = {
        "accept": "text/turtle",
        "User-Agent": "Mozilla/5.0 (compatible; MyPythonApp/1.0)"
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print("Fehler beim Laden:", response.status_code)
        return None

    graph = Graph()
    graph.parse(data=response.text, format="turtle")
    return graph


# ladet die custom Turtles, wenn URL angegeben, Vorgabe: SKOS:prefLabel, SKOS:broader
def load_custom_graph(ttl):
    url = ttl
    headers = {
        "accept": "text/turtle",
        "User-Agent": "Mozilla/5.0 (compatible; MyPythonApp/1.0)"
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code != 200:
        print("Fehler beim Laden:", response.status_code)
        return None

    graph = Graph()
    graph.parse(data=response.text, format="turtle")
    return graph


# ladet lokal heruntergeladene Turtles, Vorgabe: SKOS:prefLabel, SKOS:broader
def load_custom_graph_from_text(turtle_text):
    g = Graph()
    try:
        g.parse(data=turtle_text, format="turtle")
        return g
    except Exception as e:
        print(f"Fehler beim Parsen der Turtle-Daten: {e}")
        return None