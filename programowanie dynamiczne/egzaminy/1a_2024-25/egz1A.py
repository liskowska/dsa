"""
O((n+m)log(n+m))
coś nie działa
nwm
"""
from queue import PriorityQueue
from egz1Atesty import runtests

def battle(P,K,R):
    n = len(P)
    m = len(K)

    # C = <poczatek zasięgu katapulti i; koniec zasiegu katapulty i>
    C = [[0, 0] for _ in range(m)]
    for i in range(m):
        C[i] = [K[i], K[i] + R[i]]

    Q = PriorityQueue()

    #sortuję C po pierwszej współrzędnej i sortuję P
    def func(val): return val[0]
    C.sort(key=func)
    P.sort()

    cnt = 0
    j = 0
    for i in range(n):

        # dopisujemy do Q wszystkie katapulty, znajdujace sie przed P[i]
        while j < m and C[j][0] < P[i]:
            x, y = C[j]
            Q.put((-x, y))
            j += 1

        # Jeśli w kolejce została chociaż jedna katapulta, to powinna zostać użyta do ataku
        # kolejnego procesora (jeśli jest to w jej zasięgu)
        # if Q.empty(): continue
        # x, y = Q.get()
        # x = -x
        # if y > P[i]:
        #     cnt += 1

        # if Q.empty(): continue
        while not Q.empty():
            x, y = Q.get()
            x = -x
            if y > P[i]:
                cnt += 1
                break


    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )

# P = [14, 16, 0, 6, 10, 8]
# K = [2, 12, 4]
# R = [8, 5, 3] #3
# print(battle(P, K, R))