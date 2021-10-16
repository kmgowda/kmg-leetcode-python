// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        m = 3
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        path = [[0]*(n+1) for _ in range(m+1)]
        prefixSum = [0]*(n+1)

        s = 0
        for i in range(1, n+1):
            s += nums[i - 1]
            prefixSum[i] = s

        for i in range(1, 4):
            for j in range(k, n+1): # start with frame ending in [k, n]
                # check to either include the current interval ending here
                # or exclude the current interval ending here
                # include = curren window sum ending at j + max sum previous row with k distance away
                include = prefixSum[j] - prefixSum[j-k] + dp[i-1][j-k] if j - k >= 0 else prefixSum[j]
                exclude = dp[i][j - 1] # take previous value
                if include > exclude:
                    dp[i][j] = include
                    path[i][j] = j - k
                else:
                    dp[i][j] = exclude
                    path[i][j] = path[i][j - 1]

        # trace the path backward
        res = [None]*3
        res[2] = path[3][-1]
        res[1] = path[2][res[2]]
        res[0] = path[1][res[1]]
        return res