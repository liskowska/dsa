# (najdłuższy podciąg rosnący) Proszę rozwiązać dwa następujące zadania:
# 1. Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
# najdłuższego rosnącego podciągu?
# 2. Na wykładzie podaliśmy algorytm działający w czasie O(n^2). Proszę podać algorytm o złożoności O(nlog n).

def len_LCS(A, B):
    n = len(A)
    m = len(B)
    L = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]: L[i][j] = 1 + L[i-1][j-1]
            else: L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[n][m]

# 1. Można stworzyć drugą tablicę, która będzie posortowaną tablicą wyjściową bez duplikatów,
# a następnie wykonać na nich LCS
# złożoność obliczeniowa O(n^2)

def LIS_viaLCS(A):
    B = sorted(set(A))
    return len_LCS(A, B)

A = [7, 3, 4, 2, 6, 9, 5, 9, 10]
print(LIS_viaLCS(A))

# 2. T[i] to najmniejszy możliwy ostatni element rosnącego podciagu długości i+1 ==> len(T) = len(LIS)

def binary_search(T, low, high, x):
    # Zwraca najmniejszy indeks i, dla którego T[i] >= x
    while low <= high:
        mid = (low + high) // 2
        if T[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low  # miejsce, gdzie x powinno trafić

def LIS_nlogn(A):
    T = []
    for x in A:
        i = binary_search(T, 0, len(T)-1, x)
        print(x, i)
        if i == len(T): T.append(x)
        else: T[i] = x
        print(T)
    return len(T)

print(LIS_nlogn(A))


