# LCS - longest common subsequence - najdłuższy wspólny podciąg
# Mamy dane dwie tablice, A[n] i B[m]. Należy znaleźć długość ich najdłuższego wspólnego podciągu.
# (Klasyczny algorytm dynamiczny O(n*m)).

# długość najdłuższego LCS rekurencyjnie
def rek_LSClen(A, B, i, j):
    if i >= len(A) or j >= len(B): return 0
    elif A[i] == B[j]: return 1 + rek_LSClen(A, B, i+1, j+1)
    else: return max(rek_LSClen(A, B, i+1, j), rek_LSClen(A, B, i, j+1))

# długość najdłuższego LCS dynamicznie
def len_LCS(A, B):
    n = len(A)
    m = len(B)
    L = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]: L[i][j] = 1 + L[i-1][j-1]
            else: L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[n][m]

A = "ALIBABA"
B = "KALIMALBA"

print(rek_LSClen(A, B, 0, 0))
print(len_LCS(A, B))
