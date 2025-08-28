from kol3testy import runtests

def parkiet(B, C, s):
    n = len(C)
    m = len(C[0])
    if n == 1 and m == 1:
        if C[0][0] <= s: return 1
        else: return -1
    if n == 1: return parkiet(B[0][1:], C[0][1:], s)
    if m == 1: return parkiet(B[1:], C[1:], s)

    if C[0][0] - C[0][1] <= s and C[0][1] <= s:
         return 0
    elif C[1][0] <= s and C[0][0] - C[1][0] <= s: return 1

    else:
        B_new = [row[1:] for row in B]
        C_new = [row[1:] for row in C]
        return 1 + min(parkiet(B_new, C_new, s), parkiet(B[1:], C[1:], s))


def parkiet2(B, C, s):
    n, m = len(C), len(C[0])

    def dfs(i, j):
        if i == n-1 and j == m-1:  # jesteśmy w prawym dolnym rogu
            return 1 if C[i][j] <= s else float('inf')

        best = float('inf')

        # ruch w prawo
        if j+1 < m and abs(C[i][j] - C[i][j+1]) <= s and C[i][j+1] <= s:
            best = min(best, 1 + dfs(i, j+1))

        # ruch w dół
        if i+1 < n and abs(C[i][j] - C[i+1][j]) <= s and C[i+1][j] <= s:
            best = min(best, 1 + dfs(i+1, j))

        return best

    res = dfs(0, 0)
    return res if res != float('inf') else -1

#runtests(parkiet, all_tests = False)

B = [[2, 1, 4], [1, 3, 1], [2, 3, 3]]
C = [[20, 15, 8], [13, 10, 4], [8, 6, 3]]
s = 5

B = [(2, 1, 4),
     (1, 3, 1),
     (2, 3, 3)]

B_new = [row[1:] for row in B]

b1 = [[1, 2, 3]]

b2 = [[1],
      [2],
      [3]]

print(B_new)
print(parkiet2(B, C, s))
