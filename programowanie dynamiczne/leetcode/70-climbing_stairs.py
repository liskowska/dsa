"""
analogiczne do liczb Fibonacci
"""

def climbStairs( n: int) -> int:
    if n == 0: return 1
    elif n == 1: return 1
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

def climbStairs2( n: int) -> int:
    steps = [-1 for _ in range(n+1)]
    steps[0] = 1
    steps[1] = 1
    for i in range(2, n+1):
        steps[i] = steps[i - 1] + steps[i - 2]
    return steps[n]

print(climbStairs(10))
print(climbStairs2(10))