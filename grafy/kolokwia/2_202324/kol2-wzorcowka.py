from kol2testy import runtests

def to_list(G):
    n = 0
    for v, u, _w in G:
        n = max(n, v, u)
    n += 1

    graph_list = [[] for _ in range(n)]
    for v, u, w in G:
        graph_list[v].append((u, w))
        graph_list[u].append((v, w))

    return graph_list

from collections import deque
def BFS_status(G, s, t):
    n = len(G)
    d = [[float('inf')]*17 for _ in range(n)]
    Q = deque()
    Q.append((s, 0, 16, 0)) # v, d, stan, czas do konca krawedzi

    while Q:
        v, dist, time_left, travel_left = Q.pop()
        if travel_left != 0:
            Q.appendleft((v, dist, time_left, travel_left-1))
            continue

        if dist > d[v][time_left]: continue

        d[v][time_left] = dist
        for u, w in G[v]:
            if time_left - w >= 0 and d[u][time_left - w] > dist + w:
                Q.appendleft((u, dist + w, time_left - w, w))

        if d[v][16] > dist + 8: Q.appendleft((v, dist + 8, 16, 16))

    return min(d[t])


def BFS_throttling(G,s,t):
    n = len(G)
    time=[ [float('inf')] * 17 for _ in range(n) ]  #time[v][d] czas podrozy do wierzcholka v ze stanem d

    q = deque()
    q.append((s,0,0,0)) #(v, step, ile_h_wpodrozy, dystans do tego wierzcholka od s)
    time[0][0] = 0

    while q:
        u, step, tiredness, dystans = q.popleft()
        if step > 0:    #step to nasze opozniacze
            q.append((u,step-1,tiredness,dystans))
            continue

        for v,w in G[u]:
            if tiredness+w>16:  #musimy spac
                  n_stan = w
                  n_step = w + 8    #musimy odczekac czas przejazdu +czas spania
                  n_dys = w + 8 + dystans
            else:
                  n_stan = tiredness + w
                  n_step = w
                  n_dys = w + dystans
            if time[v][n_stan] > n_dys:   #mozna dojsc szybciej niz doszlismy wczesniej
                  time[v][n_stan] = n_dys
                  q.append((v, n_step-1, n_stan, n_dys))  #dodaje do kolejki pamietajac o opozniaczach(to byl jeden krok opozniacza wiec -1)
    return min(time[t])

def warrior(G, s, t):
    g1 = to_list(G)
    return BFS_throttling(g1, s, t)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = False  )