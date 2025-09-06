"""
494. Target sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums
and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build
the expression "+2-1". Return the number of different expressions that you can build, which evaluates to target.

Uwaga: trzeba wykorzystać WSZYSTKIE liczby z tablicy
"""

def findTargetSumWays(nums, target):
    if target < 0: target = -target
    n = len(nums)
    cnt = 0
    mem = {}
    if n == 1:
        if nums[0] == 0 == target: return 2
        if nums[0] == target: return 1
        else: return 0

    def rec(i, cur_sum):
        nonlocal cnt
        #if (i, cur_sum) in mem: return
        mem[(i, cur_sum)] = True
        if i == n - 1 and cur_sum == target:
            cnt += 1
            return
        elif i == n - 1: return

        rec(i + 1, cur_sum + nums[i])
        rec(i + 1, cur_sum - nums[i])

    rec(-1, 0)
    return cnt

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))