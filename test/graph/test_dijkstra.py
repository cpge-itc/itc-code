from cpge import dijkstra

def test_dijkstra():
    inf = float("inf")
    G = [[inf, 2, inf, inf, inf, inf, 2, inf],
 [1, inf, inf, inf, 6, inf, inf, inf],
 [inf, inf, inf, inf, inf, inf, inf, inf],
 [3, inf, inf, inf, inf, inf, inf, inf],
 [inf, 4, 2, inf, inf, inf, inf, inf],
 [inf, 2, 1, inf, inf, inf, inf, inf],
 [inf, 3, 8, 4, 8, inf, inf, 6],
 [5, inf, inf, inf, 5, 6, inf, inf]]
    assert dijkstra(G, 0) == [0, 2, 10, 6, 8, 14, 2, 8]
