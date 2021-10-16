// https://leetcode.com/problems/wiggle-sort

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        even = True
        for i in range(len(nums)-1):
            if even:
                if nums[i] > nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
            else:
                if nums[i] < nums[i+1]:
                    nums[i+1], nums[i] = nums[i], nums[i+1]
            even = not even        
        return nums            
        