import pytest
from cpge import dijkstra, astar

@pytest.fixture
def graph_ex():
    inf = float("inf")
    return [
        [inf, 2, inf, inf, inf, inf, 2, inf],
        [1, inf, inf, inf, 6, inf, inf, inf],
        [inf, inf, inf, inf, inf, inf, inf, inf],
        [3, inf, inf, inf, inf, inf, inf, inf],
        [inf, 4, 2, inf, inf, inf, inf, inf],
        [inf, 2, 1, inf, inf, inf, inf, inf],
        [inf, 3, 8, 4, 8, inf, inf, 6],
        [5, inf, inf, inf, 5, 6, inf, inf]
    ]

def test_dijkstra(graph_ex):
    assert dijkstra(graph_ex, 0) == [0, 2, 10, 6, 8, 14, 2, 8]

def test_astar(graph_ex):
    dist = dijkstra(graph_ex, 0)
    for t in range(len(graph_ex)):
        assert astar(graph_ex, 0, t, lambda v: 0) == dist[t]
