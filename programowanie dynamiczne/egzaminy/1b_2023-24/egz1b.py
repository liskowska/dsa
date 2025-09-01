from functools import lru_cache
from egz1btesty import runtests

def kstrong_rec(T, k):
    inf = -1e9
    n = len(T)
    @lru_cache(None)
    def rec(i, kr):
        if i >= n: return 0
        if kr < 0: return inf
        return T[i] + max(rec(i+1, kr), rec(i+2, kr-1))

    maxi = inf
    for j in range(n):
        maxi = max(maxi, rec(j, k))
    return maxi

# def kstrong( T, k):
#     # tu prosze wpisac wlasna implementacje
#     return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong_rec, all_tests = False)
