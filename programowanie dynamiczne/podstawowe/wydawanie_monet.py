# Zadanie 6. (wydawanie monet)
# Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T.
# Proszę podać algorytm, który oblicza minimalną ilość monet potrzebną do wydania kwoty T
# (algorytm zachłanny, wydający najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15
# jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5).

def wydawanie_monet2(A, x):
    INF = float('inf')
    dp = [INF] * (x + 1)
    dp[0] = 0  # 0 monet, by osiągnąć sumę 0

    for coin in A:
        for j in range(coin, x + 1):
            if dp[j - coin] + 1 < dp[j]:
                dp[j] = dp[j - coin] + 1
        print(dp)

    return dp[x] if dp[x] != INF else -1  # -1 jeśli nie da się wydać

A = [8, 5, 2]
print(wydawanie_monet2(A, 15))