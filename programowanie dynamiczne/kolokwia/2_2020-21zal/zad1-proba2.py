from zad1testy import runtests

def common_coordinates(A, B):
    if A == B: return A
    elif A is None or B is None: return None
    x1, y1, x2, y2, ia = A
    a1, b1, a2, b2, ib = B
    cor = [max(x1, a1), max(y1, b1), min(x2, a2), min(y2, b2), ia]

    pole = (cor[0] - cor[2]) * (cor[1] - cor[3])
    if pole < 0: return None
    return cor

def area(A):
    if A is None: return 0
    else: return (A[2] - A[0]) * (A[3] - A[1])


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
    print("d2: " ,D2)

    rect_front = [[-1, -1, -1, -1] for _ in range(n)]
    for i in range(n):
        if i == 0: rect_front[0] = D2[0]
        else: rect_front[i] = common_coordinates(rect_front[i-1], D2[i])

    rect_back = [[-1, -1, -1, -1] for _ in range(n)]
    for i in range(n-1, -1, -1):
        if i == n-1: rect_back[i] = D2[i]
        else: rect_back[i] = common_coordinates(rect_back[i+1], D2[i])

    print(rect_front)
    print(rect_back)

    maxi = -1e9
    maxi_index = -1
    for i in range(n):
        if i == 0: rect = rect_back[i+1]
        if i == n-1: rect = rect_front[i-1]
        else: rect = common_coordinates(rect_front[i-1], rect_back[i+1])
        rect_area = area(rect)
        if rect_area > maxi:
            maxi = rect_area
            maxi_index = D2[i][4]
    return maxi_index

runtests(rect)

# D = [(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]
# print(rect(D))