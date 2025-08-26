"""
62. Unique paths
There is a robot on an m x n grid. The robot is initially located in the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either
down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach
the bottom-right corner.
"""

def uniquePathsRec(m, n):
    if m == 1 or n == 1: return 1
    def rec(i, j):
        if i == m-1 and j == n - 1: return 0
        elif i == m-1: return 1
        elif j == n-1: return 1
        else: return rec(i+1, j) + rec(i, j+1)
    return rec(0, 0)

def uniquePathsDp(m, n):
    if m == 1 or n == 1: return 1
    dp = [[1 for _ in range(n)] for _ in range(m)]
    dp[m-1][n-1] = 0
    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = dp[i][j+1] + dp[i+1][j]
    return dp[0][0]

m = 3
n = 7 # 28

print(uniquePathsRec(m, n))
print(uniquePathsDp(m, n))

m2= 3
n2 = 2 # 3

print(uniquePathsRec(m2, n2))
print(uniquePathsDp(m2, n2))

print(uniquePathsRec(1, 1))
print(uniquePathsDp(1, 1))