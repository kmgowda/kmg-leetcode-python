// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        nums_1=nums[1:]
        nums_2=nums[:-1]
        def rob1(arr):
            dp = [0 ] * len(arr)
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,len(arr)):
                dp[i]=max(dp[i-1],dp[i-2]+arr[i])
            return dp[-1]
        return max(rob1(nums_1),rob1(nums_2))     
            