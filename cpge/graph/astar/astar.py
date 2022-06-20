from cpge import PriorityQueue
import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import matplotlib
from IPython.display import HTML
from copy import deepcopy

def generate_grid(n):
    rng = default_rng()
    G = np.zeros((n, n))
    for i, j in rng.normal((n/2, n/2), 2., (3*n, 2)):
        i = max(min(round(i), n - 1), 0)
        j = max(min(round(j), n - 1), 0)
        G[i, j] = 1
    G[-1, -1] = 0
    return G

def astar(G, h):
    G = deepcopy(G)
    n = len(G)
    dist = [[float("inf")]*n for _ in range(n)]
    pred = [[None]*n for _ in range(n)]
    dist[0][0] = 0
    frames = [G]
    q = PriorityQueue()
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0:
                q.add((i, j), dist[i][j])

    while not q.is_empty():
        i, j = q.take_min()
        G[i][j] = 3
        frames.append(deepcopy(G))
        if i == n - 1 and j == n - 1:
            while (i, j) != (0, 0):
                frames[-1][i][j] = 3
                i, j = pred[i][j]
            frames[-1][0][0] = 3
            break
        for i_, j_ in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= i_ < n and 0 <= j_ < n and G[i_][j_] == 0 and (i_, j_) in q:
                if dist[i][j] + 1 < dist[i_][j_]:
                    dist[i_][j_] = dist[i][j] + 1
                    q.update((i_, j_), dist[i_][j_] + ((n - i_)**2 + (n - j_)**2))
                    pred[i_][j_] = (i, j)
        G[i][j] = 2
    return frames

def anim_astar(G, h):
    fig, ax = plt.subplots()

    def update(frame):
        from matplotlib.colors import ListedColormap
        ax.clear()
        ax.set_facecolor('white')
        ax.axis('off')
        ax.axis('equal')
        ax.axis('auto')
        cmap = ListedColormap(["lightgray", "black", "skyblue", "limegreen"])
        ax.imshow(frame, interpolation='nearest', cmap=cmap)

    ani = matplotlib.animation.FuncAnimation(fig, update, frames=astar(G, h), interval=200, repeat=False)
    return HTML(ani.to_jshtml())
