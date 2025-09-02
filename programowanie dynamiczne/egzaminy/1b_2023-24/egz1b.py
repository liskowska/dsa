from egz1btesty import runtests

def kstrong_rec(T, k):
    inf = -1e9
    n = len(T)
    mem = {}
    def rec(i, kr):
        if i == n: return 0
        if kr < 0: return inf

        if (i, kr) not in mem:
            mem[(i, kr)] = max(T[i] + rec(i+1, kr), rec(i+1, kr-1), T[i]) #ide do nastepnego, skipuje i, obecny (nie ide dalej, zostaje przy tym co jest)

        return mem[(i, kr)]

    maxi = inf
    for j in range(n):
        maxi = max(maxi, rec(j, k))
    return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong_rec, all_tests = True)
