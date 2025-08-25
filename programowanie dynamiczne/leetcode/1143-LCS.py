"""
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.
If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none)
deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
"""

def lcsRec(text1, text2):
    n = len(text1)
    m = len(text2)
    def rec(i, j):
        if i == n or j == m: return 0
        elif text1[i] == text2[j]: return 1 + rec(i+1, j+1)
        else: return max(rec(i+1, j), rec(i, j+1))
    return rec(0, 0)

def lcsDp(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
            else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m]

text1 = "abcde"
text2 = "ace"
print(lcsDp(text1, text2))