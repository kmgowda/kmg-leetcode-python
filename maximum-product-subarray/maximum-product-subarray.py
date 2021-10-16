// https://leetcode.com/problems/maximum-product-subarray

class Solution(object):
    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ma = nums[0] 
        for i in range(0, n):
            p = nums[i]
            ma= max(ma, p)    
            for j in range(i+1, n):
                p*=nums[j]
                ma= max(ma, p)
        return ma   

    def maxProduct(self, nums):
        ma=big=small=nums[0]
        for n in nums[1:]:
            big, small=max(n, n*big, n*small), min(n, n*big, n*small)
            ma=max(ma, big)
        return ma    