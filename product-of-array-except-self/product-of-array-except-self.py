// https://leetcode.com/problems/product-of-array-except-self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod =[1]*len(nums)
        for i in range(1, len(nums)):
            prod[i] = prod[i-1]*nums[i-1]
        cur = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            prod[i]*=cur
            cur*=nums[i]
        return prod    
        