// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums)-1
        
        while l <= h:
            
            while nums[l] == nums[h] and l < h:
                l+=1
            
            if nums[l] <= nums[h]:
                return nums[l]
            
            m = (l+h)//2
            if nums[m] > nums[h]:
                l = m+1
            else:
                h = m
                
        return nums[l]        