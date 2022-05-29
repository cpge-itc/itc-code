import networkx as nx
import random
import itertools


def random_nx(n=8, p=0.35, directed=False):
    return nx.fast_gnp_random_graph(n, p, directed=directed)


def random_matrix(n=8, p=0.35, directed=False, weighted=False):
    G = [[float("inf") if weighted else 0] * n for _ in range(n)]
    for i, j in itertools.combinations_with_replacement(range(n), 2):
        if i == j: continue
        if not directed:
            G[i][j] = G[j][i]
        if random.random() < p:
            G[i][j] = random.randrange(1, 10) if weighted else 1
        if random.random() < p:
            G[j][i] = random.randrange(1, 10) if weighted else 1
    return G
