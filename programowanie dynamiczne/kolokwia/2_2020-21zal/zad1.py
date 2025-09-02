def pole(A, B):

    if A == B == None: return [0, None]
    elif A == None: return [0, None]
    elif B == None: return [0, None]

    x1, y1, x2, y2, ia = A
    a1, b1, a2, b2, ib = B
    wsp = [max(x1, a1), max(y1, b1), min(x2, a2), min(y2, b2), ia]

    pole = (wsp[0] - wsp[2]) * (wsp[1] - wsp[3])
    if pole < 0:
        pole = 0
        wsp = None

    print(pole, wsp)
    return pole, wsp


def rect(D):
    n = len(D)
    D2 = [[-1]*5 for _ in range(n)]
    for i in range(n):
        D2[i][0] = D[i][0]
        D2[i][1] = D[i][1]
        D2[i][2] = D[i][2]
        D2[i][3] = D[i][3]
        D2[i][4] = i #spamiętujemy oryginalny indeks

    def func0(val): return val[0]
    def func1(val): return val[1]
    def func2(val): return val[2]
    def func3(val): return val[3]

    D2.sort(key= func0)
    D2.sort(key= func1)
    D2.sort(key= func2)
    D2.sort(key= func3)
    print(D2)

    rect_front = [[0, None] for _ in range(n)]
    for i in range(n):
        if i == 0: rect_front[0] = pole(D2[0], D2[0])
        else: rect_front[i] = pole(rect_front[i-1][1], D2[i])

    rect_back = [[0, None] for _ in range(n)]
    for i in range(n-1, -1, -1):
        if i == n-1: rect_back[n-1] = pole(D2[n-1], D2[n-1])
        else: rect_back[i] = pole(rect_back[i+1][1], D2[i])

    mini = float('inf')
    mini_index = -1
    cur_pole, rect = pole(D2[0], D2[0])
    for i in range(n):
        cur_pole, rect = pole(rect_front[i][1], rect_back[i][1])
        print(cur_pole)
        if cur_pole <= mini:
            mini = cur_pole
            mini_index = D2[i][4]
    print(rect_front)
    print(rect_back)
    return mini_index

D = [(2,3,10,6),(3,1,8,8),(5,4,9,7)]
print(rect(D))
#
# D2 = [(0,1,2,2),(3,1,8,8),(5,4,9,7)]
# print(rect(D2))