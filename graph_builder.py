import os
import networkx as nx

def build_graph_from_docs(documents):
    G = nx.DiGraph()
    for doc in documents:
        title = doc['title']
        G.add_node(title, content=doc['content'])
        for link in doc.get('related', []):
            G.add_edge(title, link)
    return G

def save_graphml(graph, path='graph/context_graph.graphml'):
    nx.write_graphml(graph, path)

def load_graphml(path='graph/context_graph.graphml'):
    return nx.read_graphml(path)