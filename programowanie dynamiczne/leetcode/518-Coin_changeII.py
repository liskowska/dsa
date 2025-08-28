"""
518. Coin Change II
You are given an integer array coins representing coins of different denominations and an integer amount
representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up
 by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer
"""

def change_rec(amount, coins):
    n = len(coins)
    coins.sort()
    def rec(i, amount):
        if i >= n: return 0
        elif amount == 0: return 1
        elif amount < 0: return 0

        res = 0
        if amount >= coins[i]:
            res = rec(i+1, amount)
            res += rec(i, amount - coins[i])
        return res
    return rec(0, amount)

def change_dp(amount, coins):
    n = len(coins)
    m = amount
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    coin = 0
    for i in range(1, n+1):
        coin = coins[i-1]
        for j in range(m+1):
            if j - coin < 0: dp[i][j] = dp[i-1][j]
            else :dp[i][j] = dp[i-1][j] + dp[i][j-coin]
    return dp[n][m]

a1 = 5
coins1 = [1,2,5] # 4
print(change_rec(a1, coins1))
print(change_dp(a1, coins1))