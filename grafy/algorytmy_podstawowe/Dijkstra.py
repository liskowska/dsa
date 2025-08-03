"""
założenie: wagi krawędzi są dodatnie
złożoność czasowa:
 - O(ElogV) dla reprezentacji listowej
 - O(V^2) dla reprezentacji macierzowej
"""
from queue import PriorityQueue
def dijkstra_list(G, s):
    n = len(G)

    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()

    d[s] = 0
    queue.put((s, d[s]))

    while not queue.empty():
        v, _d = queue.get()
        if not visited[v]:
            visited[v] = True
            for u, w in G[v]:
                if d[v] + w < d[u]: #relaksacja
                    d[u] = d[v] + w
                    parent[u] = v
                    queue.put((u, d[u]))
    return d, parent

def relax(distance, vertex, neighbour, weight):
    if distance[neighbour] > distance[vertex] + weight:
        distance[neighbour] = distance[vertex] + weight
        return True
    #
    return False
#end procedure relax


def Dijkstra(G, source):
    #
    n = len(G)
    distance = [ float('inf') for _ in range(n) ]
    parent   = [ None for _ in range(n)         ]
    done     = [ False for _ in range(n)        ]

    queue = PriorityQueue()
    queue.put( (0, source) )
    distance[source] = 0

    while not queue.empty():
        value, vertex = queue.get()

        for neighbour in range(n):
            if done[neighbour] == False:
                if G[vertex][neighbour] != -1 and relax( distance, vertex, neighbour, G[vertex][neighbour] ):
                    queue.put( (distance[neighbour], neighbour) )
                    parent[neighbour] = vertex
        #end for
        done[vertex] = True
    #end while
    return distance

def dijkstra_matrix(G, s):
    n = len(G)

    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()

    queue.put((0, s))
    d[s] = 0

    while not queue.empty():
        _dist, v = queue.get()
        for u in range(n):
            if not visited[u]:
                if G[v][u] != -1 and d[v] + G[v][u] < d[u]:
                    d[u] = d[v] + G[v][u]
                    parent[u] = v
                    queue.put((d[u], u))
        visited[v] = True
    return d, parent

def create_shortest_path(parent, t): #parent dla dijkstra(G, s), gdzie szukamy sciezki od s do t
    v = t
    shortest_path = []
    while v is not None:
        shortest_path.append(v)
        v = parent[v]
    shortest_path.reverse()
    return shortest_path


G1 = [
    [(1, 3), (2, 5)],       # wierzchołek 0 połączony z 1 (waga 3) i 2 (waga 5)
    [(0, 3), (2, 1), (3, 4)], # wierzchołek 1 połączony z 0, 2, 3
    [(0, 5), (1, 1), (4, 7)], # wierzchołek 2 połączony z 0, 1, 4
    [(1, 4), (4, 2)],       # wierzchołek 3 połączony z 1, 4
    [(2, 7), (3, 2)]        # wierzchołek 4 połączony z 2, 3
]

G1_matrix = [
#  0    1    2    3    4
  [ 0,  3,  5, -1, -1],  # 0
  [ 3,  0,  1,  4, -1],  # 1
  [ 5,  1,  0, -1,  7],  # 2
  [-1,  4, -1,  0,  2],  # 3
  [-1, -1,  7,  2,  0]   # 4
]


print(dijkstra_list(G1, 0))
print(dijkstra_matrix(G1_matrix, 0))
print(create_shortest_path(dijkstra_list(G1, 0)[1], 4))
print(create_shortest_path(dijkstra_matrix(G1_matrix, 0)[1], 4))