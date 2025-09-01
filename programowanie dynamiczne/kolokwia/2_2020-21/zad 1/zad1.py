"""
1. Rozszerzam krotki o pierwotny indeks w akademiku
2. Sortuję kolejno
    - po początkach
    - po końcach budynków
3. Wyznaczam funkcję prev[v], która zwraca ostatni indeks akademika, który jest przed v i można go
   wybudować jednocześnie razem z v. np dla przykładu do zadania prev = [None, 0, 0]
4. Tworzę funkcję f(i,j) - Ile najwięcej studentów jestem w stanie pomieścić mając do dyspozycji
   akademiki z indeksów <0;i> mając <=x pieniędzy.

coś nie działa. Nie mam siły do tego algorytmu.
"""

from zad1testy import runtests

def select_buildings(T, p):
    new_T = [['h', 'a', 'b', 'w', 'i'] for _ in range(len(T))]
    for i in range(0, len(T)):
        new_T[i][0] = T[i][0]
        new_T[i][1] = T[i][1]
        new_T[i][2] = T[i][2]
        new_T[i][3] = T[i][3]
        new_T[i][4] = i

    def func1(val): return val[1]
    def func2(val): return val[2]
    new_T.sort(key = func1)
    new_T.sort(key = func2)

    prev = [None for _ in range(len(new_T))]
    for i in range(len(new_T)):
        for j in range(i-1, -1, -1):
            if new_T[j][2] <= new_T[i][1]:
                prev[i] = j
                break

    n = len(new_T)
    dp = [[[0, 0] for _ in range(p+1)] for _ in range(n)]
    ans = []
    for i in range(0, n):
        students = new_T[i][0] * ( new_T[i][2] - new_T[i][1] )
        for j in range(1, p+1):
            if prev[i] is None:
                dp[i][j] = dp[i][j - 1]
                if new_T[i][3] <= j and dp[i][j][0] < students: dp[i][j] = [students, new_T[i][3]]
            else:
                if new_T[i][3] <= j and dp[i][j][0] <= students:
                    dp[i][j] = [students, new_T[i][3]]

                diff = j - dp[i][j-1][1]
                dp[i][j][0] = max(dp[prev[i]][diff][0] + dp[i][j-1][0], dp[i][j][0])
                if dp[i][j][0] == dp[prev[i]][diff][0] + dp[i][j-1][0]:
                    dp[i][j][1] = dp[prev[i]][diff][1] + dp[i][j-1][1]

    maxi, index = 0, -1
    for i in range(n):
        if maxi < dp[i][p][0]:
            maxi = dp[i][p][0]
            index = i
    print(maxi)

    ans = []
    while index is not None:
        for j in range(p, 0, -1):
            if dp[index][j][0] == dp[index][j-1][0]: continue
            ans.append(new_T[index][4])
            break
        index = prev[index]
    return ans

runtests( select_buildings )

tab = [(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
p = 6
print(select_buildings(tab, p))
