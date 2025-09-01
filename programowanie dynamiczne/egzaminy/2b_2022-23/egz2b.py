"""
złożoność czasowa O(nk) - wzorcowa
f(i, j) - minimalna suma odległości biurowców z pozycji od X[0] do X[i] do przydzielonych im działek
od Y[0] do Y[j]. W momencie obliczania f(i, j) możemy działce X[i] przydzielić działkę Y[j] albo ją
odrzucić i zostać przy obecnie mniejszej (lepszej) sumie
"""
from egz2btesty import runtests

def parking(X,Y):
    n = len(X)
    m = len(Y)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):

            # odległość między biurowcem i a parkingiem j
            d = abs(Y[j-1] - X[i-1])

            if j <= i:
                if i == 1: dp[i][j] = d
                elif i == j: dp[i][j] = dp[i][j-1] + d
                else: dp[i][j] = dp[i-1][j]
            elif i == 1: dp[i][j] = min(d, dp[i][j-1])
            else: dp[i][j] = min(dp[i-1][j-1] + d, dp[i][j-1])
    return dp[n][m]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
