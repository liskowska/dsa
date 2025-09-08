"""
złożoność akceptowalna O(n^2) - sprawdzanie każdego przedziału z każdym, dopóki nie znajdziemy pary niefajnej
złożoność wzorcowa O(nlogn) wsm nwm. Chyba napisałam O(n^2). Na wzorcówkę by trzeba było korzystać z jakichś
fancy struktur danych :((.
"""

from egz3btesty import runtests

def uncool( P ):
    #rozszerzam P o oryginalny indeks
    n = len(P)
    for i in range(n):
        P[i].append(i)

    # sortuje najpierw po końcach, później po początkach
    def func_k(val): return val[1]
    def func_p(val): return val[0]
    P.sort(key = func_k)
    P.sort(key = func_p)

    iteration = -1
    for x1, y1, i1 in P:
        iteration += 1
        for j in range(n-1, iteration, -1):
            x2, y2, i2 = P[j]
            if x1 == x2 or y1 == y2: continue #przedział w przedziale
            if y1 >= x2 and y1 < y2: return i1, i2
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
