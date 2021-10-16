// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        h = len(nums)-1
        found = False
        
        while l <= h and not found:
            m = (l+h)//2
            
            if nums[m] == target:
                found = True  
            elif target < nums[m]:
                h = m-1
            else:
                l = m+1
        if not found:
            return [-1, -1]
        s = m
        while s > -1 and nums[s] == target:
            s -=1
        e = m
        while e < len(nums) and nums[e] == target:
            e+=1
        return [s+1,e-1]    
               
                