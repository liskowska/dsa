"""
213. House Robber II
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security
system connected, and it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of
money you can rob tonight without alerting the police.
"""

def rob2_rek(nums):
    def rek(n, flag):
        if n >= len(nums): return 0
        elif n == len(nums) - 1 and flag is True: return 0
        else: return nums[n] + max(rek(n+2, flag), rek(n+3, flag))
    return max(rek(0, True), rek(1, False))


def rob2_dp(nums):
    if len(nums) == 1: return nums[0]
    memo = [[-1]*2 for _ in range(len(nums))]

    def rec(i, flag):
        if i >= len(nums) or (flag and i == len(nums)-1): return 0
        if memo[i][flag] != -1: return memo[i][flag] #spamiętywanie
        memo[i][flag] = max(rec(i+1, flag), nums[i] + rec(i+2, flag ))

        return memo[i][flag]
    return max(rec(0, True), rec(1, False))


nums = [1,2,3,1]
print(rob2_rek(nums))
print(rob2_dp(nums))

nums2 = [2,7,9,3,1]
print(rob2_rek(nums2))
print(rob2_dp(nums2))

nums3 = [1, 1, 1]
print(rob2_rek(nums3))
print(rob2_dp(nums3))

nums4 = [1,2,1,1]
print(rob2_rek(nums4))
print(rob2_dp(nums4))

