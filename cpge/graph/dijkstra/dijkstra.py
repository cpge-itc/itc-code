from cpge import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    dist = [float("inf")]*n
    dist[s] = 0
    q = PriorityQueue()
    for v in range(n):
        q.add(v, dist[v])
    while not q.is_empty():
        u = q.take_min()
        for v in range(n):
            d = dist[u] + G[u][v]
            if v in q and d < dist[v]:
                q.update(v, d)
                dist[v] = d
    return dist
