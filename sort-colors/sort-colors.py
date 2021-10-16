// https://leetcode.com/problems/sort-colors

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=tmp
                    