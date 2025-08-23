"""
746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of i-th step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""
def minCostClimbingStairs(A):
    n = len(A)
    A.append(0)
    cost = [-1 for _ in range(n+1)]
    cost[0] = A[0]
    cost[1] = A[1]

    for i in range(2, n+1):
        cost[i] = A[i] + min(cost[i-1], cost[i-2])
    return min(cost[n], cost[n-1])

def minCostClimbingStairs2(A):
    def rec(i):
        if i >= len(A): return 0
        else: return A[i] + min(rec(i+1), rec(i+2))
    return min(rec(0), rec(1))

e1 = [10, 15, 20] # 15
e2 = [1,100,1,1,1,100,1,1,100,1] # 6

print(minCostClimbingStairs2(e1))
print(minCostClimbingStairs(e1))
print(minCostClimbingStairs2(e2))
print(minCostClimbingStairs(e2))