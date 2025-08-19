"""
787. Cheapest Flights Within K Stops
There are n cities connected by some number of flights. You are given an array flights where
flights[i] = [from, to, price] indicates that there is a flight from city 'from' to city 'to' with cost 'price'.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
If there is no such route, return -1.
"""

from queue import PriorityQueue
def dijkstra_list_status(G, s, t, k): # k - maximum stops that can be made
    n = len(G)

    d = [[float('inf')]*(k+2) for _ in range(n)]
    parent = [None for _ in range(n)]
    #visited = [False for _ in range(n)]
    #stops = [float('inf') for _ in range(n)]

    queue = PriorityQueue()

    d[s][0] = 0
    queue.put((d[s][0], s, 0)) #odleglosc, wierzcholek, dlugosc krawedzi

    while not queue.empty():
        dist, v, st = queue.get()
        if v == t: return dist

        if st == k + 1 : continue
        if dist > d[v][st]: continue

        for u, w in G[v]:
            new_dist = dist + w
            new_st = st + 1
            if new_dist < d[u][st+1]:  #relaksacja
                d[u][st+1] = new_dist
                parent[u] = v
                queue.put((new_dist, u, new_st))
    return -1

def to_list(edges, n):
    list = [[] for _ in range(n)]
    for u, v, w in edges:
        list[u].append((v, w))
    return list


def findCheapestPrice(n, flights, src, dst, k):
    G = to_list(flights, n)
    distances = dijkstra_list_status(G, src, dst, k)
    return distances

n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))

flights2 = [[1,0,5],[2,1,5],[3,0,2],[1,3,2],[4,1,1],[2,4,1]]
n2 = 5
src2 = 2
dst2 = 0
k2 = 2
print(findCheapestPrice(n2, flights2, src2, dst2, k2))

flights3 = [[0,1,1],[1,2,1],[2,3,1],[3,7,1],[0,4,3],[4,5,3],[5,7,3],[0,6,5],[6,7,100],[7,8,1]]
n3 = 9
src3 = 0
sdt3 = 8
k3 = 3
print(findCheapestPrice(n3, flights3, src3, sdt3, k3))
