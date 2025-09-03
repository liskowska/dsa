from zad1testy import runtests

def start_x(I, x):
    n = len(I)
    can_reach = [False for _ in range(n)]
    def rec(i, prev_b):
        (a, b), index = I[i]
        if can_reach[index] is True: return
        else:
            if i == n-1:
                if prev_b == a: can_reach[index] = True
                return
            if prev_b == a:
                can_reach[index] = True
            rec(i+1, a)
            rec(i+1, prev_b)

    i = 0
    while I[i][0][0] <= x:
        if I[i][0][0] < x:
            i += 1
            continue
        else:
            can_reach[I[i][1]] = True
            rec(i+1, I[i][0][1])
            i += 1
    return can_reach

def end_y(I, y):
    n = len(I)
    can_reach = [False for _ in range(n)]

    def rec(i, prev_a):
        (a, b), index = I[i]
        if can_reach[index] is True: return
        if i == 0:
            if prev_a == b: can_reach[index] = True
            return
        if prev_a == b:
            can_reach[index] = True
        rec(i-1, a)
        rec(i-1, prev_a)

    i = n-1
    while I[i][0][1] >=y:
        if I[i][0][1] > y:
            i -= 1
            continue
        else:
            can_reach[I[i][1]] = True
            rec(i-1, I[i][0][0])
            i -= 1
    return can_reach

def intuse( I, x, y ):
    n = len(I)
    I_index = [[I[i], -1] for i in range(n)]
    for i in range(n):
        I_index[i][1] = i

    I_index.sort(key=lambda x: (x[0][0], x[0][1]))

    start = start_x(I_index, x)
    end = end_y(I_index, y)
    ans = []
    for i in range(n):
        if start[i] == end[i] == True: ans.append(i)
    return ans

I = [ (3,4), (2,5), (1,3), (4,6), (1,4) ]
x = 1
y = 6
print(intuse(I, x, y))

runtests( intuse )


