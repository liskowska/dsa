from functools import lru_cache

from zad1testy import runtests

def start_x(I, x):
    n = len(I)
    can_reach = [False for _ in range(n)]

    mem = {}
    def rec(i, prev_b):
        if (i, prev_b) in mem: return
        (a, b), index = I[i]
        if i == n-1:
            if prev_b == a: can_reach[index] = True
            return

        if prev_b == a:
            can_reach[index] = True
            rec(i+1, b)
            mem[(i, b)] = True
        rec(i+1, prev_b)
        mem[(i, prev_b)] = True

    rec(0, x)
    return can_reach

def end_y(I, y):
    n = len(I)
    can_reach = [False for _ in range(n)]

    mem = {}
    def rec(i, prev_a):
        if (i, prev_a) in mem: return
        (a, b), index = I[i]
        if i == 0:
            if prev_a == b: can_reach[index] = True
            return

        if prev_a == b:
            can_reach[index] = True
            rec(i-1, a)
            mem[(i, a)] = True
        rec(i-1, prev_a)
        mem[(i, prev_a)] = True #True = done

    rec(n-1, y)
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
#print(intuse(I, x, y))

runtests( intuse )


