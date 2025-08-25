

from kol3testy import runtests


def parkiet(B, C, s):
    n = len(C)
    m = len(C[0])
    if n == 1 and m == 1:
        if C[0][0] <= s: return 1
        else: return -1
    elif n == 1: return parkiet(B[1:], C[1:], s)
    elif m == 1: return parkiet(B[0:n][1:], C[0:n][1:], s)
    elif C[0][0] - C[0][1] <= s and C[0][1] <= s:
         return
    elif(C[1][0] <= s and C[0][0] - C[1][0] <= s)):
        return 1
    return -1

#runtests(parkiet, all_tests = False)

B = [(2, 1, 4),
     (1, 3, 1),
     (2, 3, 3)]

print(B[0:len(B)][1:])
