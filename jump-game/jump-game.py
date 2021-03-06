// https://leetcode.com/problems/jump-game

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 2:
            return True
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
             if dp[i-1] < i:
                    return False
             dp[i] = max(dp[i-1], i+nums[i])
    
        return True if max(dp) >= len(nums)-1 else False   
            
            