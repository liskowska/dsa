"""
założenia: graf w reprezentacji macierzowej,
    można stosować ujemne wagi (ale nie ujemne cykle)
złożoność czasowa: O(V^3) (szybkie)
"""

def floyd_warshall(G):
    n = len(G)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    return G

from math import inf
graph = [[0, 3, inf, 7],
         [8, 0, 2, inf],
         [5, inf, 0, 1],
         [2, inf, inf, 0]]

print(floyd_warshall(graph))