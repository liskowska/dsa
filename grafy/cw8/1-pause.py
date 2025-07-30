"""
Znany operator telefonii komórkowej Pause postanowił zakonczyc działalnosc w
Polsce. Jednym z głównych elementów całej procedury jest wyłaczenie wszystkich stacji nadawczych (które
tworza spójny graf połaczen). Ze wzgledów technologicznych urzadzenia nalezy wyłaczac pojedynczo a operatorowi
dodatkowo zalezy na tym, by podczas całego procesu wszyscy abonenci znajdujacy sie w zasiegu
działajacych stacji mogli sie ze soba łaczyc (czyli by graf pozostał spójny). Proszę zaproponować algorytm
podający kolejność wyłączania stacji.
"""

"""
ALgorytm sortuje topologocznie (DFS) graf zwracając kolejno przetworzone wierzchołki
"""

def topological_sort(G):
    n = len(G)
    visited = [False] * n
    topo_order = [] #

    def DFS_visit(v):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                DFS_visit(u)
        # dodajemy do sortowania po odwiedzeniu wszystkich sąsiadów
        topo_order.append(v)

    for v in range(n):
        if not visited[v]:
            DFS_visit(v)

    # ponieważ dodawaliśmy wierzchołki po odwiedzeniu dzieci (postorder), musimy odwrócić wynik
    topo_order.reverse()
    return topo_order


G = [[1, 2],
     [8],
     [3, 5],
     [4, 6],
     [],
     [8],
     [],
     [],
     [7]]
print(topological_sort(G))


def topologicalsort_matrix(G):
    n = len(G)
    visited = [False for _ in range(n)]
    topoorder = []

    def DFS_visit(G, v):
        visited[v] = True
        for u in range(n):
            if G[v][u] == 1 and not visited[u]: DFS_visit(G, u)
        topoorder.append(v)

    for v in range(n):
        if not visited[v]: DFS_visit(G, v)

    topoorder.reverse()
    return topoorder

G_matrix = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0]]

print(topologicalsort_matrix(G_matrix))