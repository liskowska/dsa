"""
O(nE)
f(i, b) - minimalny koszt znalezienia się na planecie i mając b ton paliwa
"""
from egz1btesty import runtests

def planets2(D, C, T, E):
    n = len(D)
    INF = float("inf")
    dp = [[INF]*(E+1) for _ in range(n)]
    dp[0][0] = 0

    for i in range(n):
        # tankowanie na tej planecie
        for b in range(1, E+1):
            dp[i][b] = min(dp[i][b], dp[i][b-1] + C[i])

        # loty do następnych planet
        for j in range(i+1, n):
            dist = D[j] - D[i]
            if dist > E: break
            for b in range(dist, E+1):
                dp[j][b-dist] = min(dp[j][b-dist], dp[i][b])

        # teleport (tylko przy pustym zbiorniku!)
        dest, cost_t = T[i]
        if dest != i:
            dp[dest][0] = min(dp[dest][0], dp[i][0] + cost_t)

    return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets2, all_tests = True )