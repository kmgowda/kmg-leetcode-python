// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        def rob(arr):
            dp = arr[:]
            for i in range(2, len(dp)):
                dp[i]+=max(dp[:i-1])
            return max(dp[-1], dp[-2])
 
        return rob(nums)
                
        
        
        