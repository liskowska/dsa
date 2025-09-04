# Dana jest tablica n liczb naturalnych A. Proszę podać i zaimplementować algorytm, który sprawdza,
# czy da się wybrać podciąg liczb z A, które sumują się do zadanej wartości T.
#O(nT)

def subset_sum(A, T):
    n = len(A)
    m = T+1
    N = [[False for _ in range(m)] for _ in range(n)]
    N[0][0] = True

    if A[0] <= T:
        N[0][A[0]] = True

    for i in range(1, n):
        value = A[i]
        for j in range(m):
            N[i][j] = N[i-1][j]
            if j-value >= 0 and N[i][j-value]: N[i][j] = True
    return N[n-1][T]

A = [1, 7, 10, 5, 9, 3]
print(subset_sum(A, 26))