"""
algorytm zachłanny:
1. 'spłaszczamy' tablicę do wymiarów 1xn, żeby w komórkach i znajdowała się suma całej kałuży paliwa.
    Jeżeli kałuża sięga kilka komórek pierwszego wiersza to sume wpisujemy w komórkę o najmniejszym
    indeksie, a w pozostałych komórkach pozostawiamy 0. Sprawdzamy to za pomocą algorytmu dfs.
2. Po nowo stworzonej tablicy szukamy największych plam paliwa. Tworzę kolejkę priorytetową
"""
from zad3testy import runtests
from collections import deque
from queue import PriorityQueue

def bfs(T, s, n, m, visited):
    if visited[0][s]: return 0, visited
    Q = deque()
    sum = T[0][s]

    visited[0][s] = True
    Q.append((0, s))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]] #prawo, lewo, góra, dół
    while Q:
        i, j = Q.popleft()
        for d1, d2 in directions:
            if i+d1 < 0 or i+d1 >= n or j+d2 < 0 or j+d2 >=m: continue
            if not visited[i + d1][j+ d2] and T[i+d1][j+d2] != 0:
                visited[i + d1][j + d2] = True
                sum += T[i + d1][j + d2]
                Q.append((i+d1, j+d2))
    return sum, visited

def to_path(T):
    n = len(T)
    m = len(T[0])
    path = [0 for _ in range(m)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    if n == 1: return T

    for i in range(m):
        if T[0][i] == 0: continue
        path[i], visited = bfs(T, i, n, m, visited)
    return path

def plan(T):
    path = to_path(T)
    fuel = 0
    stops = []
    index = 0
    Q = PriorityQueue()
    Q.put((-path[0], index)) #fuel, index

    while index < len(path) - 1:
        if fuel == 0:
            if Q.empty(): return None  # nie da się dojechać
            extra_fuel, stop_idx = Q.get()
            fuel += -extra_fuel
            stops.append(stop_idx)

        index += 1
        fuel -= 1
        if path[index] != 0:
            Q.put((-path[index], index))

    stops.sort()
    return stops


runtests(plan)