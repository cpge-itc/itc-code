from cpge import PriorityQueue

def astar(G, s, t, h):
    n = len(G)
    dist = n*[float("inf")]
    dist[s] = 0
    q = PriorityQueue()
    for v in range(n):
        q.add(v, dist[v])
    while not q.is_empty():
        u = q.take_min()
        if u == t:
            return dist[t]
        for v in range(n):
            d = dist[u] + G[u][v]
            if v in q and d < dist[v]:
                q.update(v, d + h(v))
                dist[v] = d
