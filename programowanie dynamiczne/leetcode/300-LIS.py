"""
300. Longest Increasing Subsequence
Given an integer array 'nums', return the length of the longest strictly increasing subsequence.
"""

def lenghtOfLIS_rec(nums):
    n = len(nums)
    def rec(i, prev):
        if i == n: return 0

        # opcja 1: pomijamy nums[i]
        best = rec(i + 1, prev)
        
        # opcja 2: bierzemy nums[i], jeśli rosnący
        if prev is None or nums[i] > prev:
            best = max(best, 1 + rec(i + 1, nums[i]))
        return best

    return rec(0, None)


def lenghtOfLIS_dp(nums):
    n = len(nums)
    dp = [1 for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

nums1 = [10,9,2,5,3,7,101,18] #4
nums2 = [0,1,0,3,2,3] #4
nums3 = [4,10,4,3,8,9] #3
nums4 = [1, 2, 4, 3] #3

print(lenghtOfLIS_rec(nums1))
print(lenghtOfLIS_rec(nums2))
print(lenghtOfLIS_rec(nums3))
print(lenghtOfLIS_rec(nums4))
print()
print(lenghtOfLIS_dp(nums1))
print(lenghtOfLIS_dp(nums2))
print(lenghtOfLIS_dp(nums3))
print(lenghtOfLIS_dp(nums4))