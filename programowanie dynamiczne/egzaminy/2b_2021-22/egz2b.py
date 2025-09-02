"""
f(i) - maksymalna liczba złota z jaką możemy się dostać do i-tej komnaty
    Sprawdzamy czy f(i) != -1. Jeśli tak to sprawdzamy wszystkie wyjścia z danej komnaty.
    current_gold - ile mamy obecnie golda
    diff = current_gold - gold_chest
    if diff < 0 and diff >= - 10 or diff >= 0 and f(i) - diff >= 0: f(u) =
    max(f[u], current_gold - diff)
"""

from egz2btesty import runtests

def magic( C ):
    n = len(C)
    dp = [-1 for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        gold_chest = C[i][0]
        cur_gold = dp[i]
        if cur_gold == -1: continue
        for j in range(1, 4):

            index = C[i][j][1]
            if index == -1: continue
            gold_to_open = C[i][j][0]
            diff = gold_to_open - gold_chest # diff > 0 - musimy dac z kieszeni do otwarcia drzwi

            if (0 > diff >= -10) or (diff >= 0 and cur_gold - diff >= 0):
                dp[index] = max(dp[index], cur_gold - diff)
    return dp[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )