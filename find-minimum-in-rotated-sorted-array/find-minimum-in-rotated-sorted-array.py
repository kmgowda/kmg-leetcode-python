// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        while nums[l] > nums[h]:
            m = (l+h)//2
            if nums[m] > nums[h]:
               l = m+1
            else:
               h = m 
 
        return nums[l]      