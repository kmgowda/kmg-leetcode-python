// https://leetcode.com/problems/burst-balloons

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def calculate(i, j):
            if dp[i][j] or j == i + 1: # in memory or gap < 2
                return dp[i][j]
            ma = 0
            for k in range(i+1, j): # find the last balloon
                ma = max(ma, nums[i] * nums[k] * nums[j] + calculate(i, k) + calculate(k, j))
            dp[i][j] = ma
            return ma

        return calculate(0, n-1)