"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses
have security systems connected, and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount
of money you can rob tonight without alerting the police.
"""

def rob_rek(nums):
    n = 0
    def rek(n):
        if n >= len(nums): return 0
        else: return nums[n] + max(rek(n+2), rek(n+3))
    return max(rek(0), rek(1))

def rob_dp(nums):
    n = len(nums)
    dp = [-1 for _ in range(n)]

    if n == 0: return 0
    if n == 1: return nums[0]

    dp[0] = nums[0]
    dp[1] = nums[1]
    for i in range(2, n):
        if i == 2: dp[i] = nums[i] + nums[i-2]
        else: dp[i] = nums[i] + max(dp[i-2], dp[i-3])
    return max(dp[n-1], dp[n-2])

nums = [1,2,3,1]
print(rob_rek(nums))
print(rob_dp(nums))

nums2 = [2,7,9,3,1]
print(rob_rek(nums2))
print(rob_dp(nums2))

nums3 = [1, 1, 1]
print(rob_rek(nums3))
print(rob_dp(nums3))
