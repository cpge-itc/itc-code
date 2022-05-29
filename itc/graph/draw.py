import networkx as nx
import matplotlib.pyplot as plt

# plt.rcParams["figure.figsize"] = (15, 8)


def draw(G, directed=False, weighted=False):
    graph_type = nx.DiGraph() if directed else nx.Graph()
    if all(map(lambda l: len(l) == len(G), G)):  # matrice d'adjacence
        import copy
        import numpy as np
        G = copy.deepcopy(np.array(G))
        G[G == float("inf")] = 0
        G = nx.from_numpy_matrix(np.array(G), create_using=graph_type)
    else:  # liste d'adjacence
        G = nx.from_dict_of_lists(G, create_using=graph_type)
        # G_ = nx.DiGraph() if directed else nx.Graph()
        # G_.add_edges_from([(i, j) for i in range(len(G)) for j in G[i]])

    plt.clf()
    pos = nx.spring_layout(G, weight=None, k=2)
    nx.draw(G,
            pos=pos,
            node_size=600,
            font_size=16,
            node_color="white",
            edgecolors="black",
            with_labels=True,
            arrowsize=35)
    if weighted:
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
    plt.show()


def draw_graph(G):
    plt.clf()
    G_ = nx.DiGraph()
    G_.add_edges_from([(i, j) for i in range(len(G)) for j in G[i]])
    nx.draw_networkx(G_, font_color="w", node_color="black", node_size=600, arrowsize=35, font_size=16)
    plt.show()


def draw_weighted_graph(G):
    pos = nx.spring_layout(G)
    options = {"font_size": 20, "node_size": 700, "edgecolors": "black", "node_color": "white"}
    nx.draw(G, pos, with_labels=True, **options)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
    plt.show()
