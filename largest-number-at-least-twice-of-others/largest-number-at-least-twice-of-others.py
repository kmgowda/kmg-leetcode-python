// https://leetcode.com/problems/largest-number-at-least-twice-of-others

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = None
        max2 = None
        max1index = None
        
        for i in range(len(nums)):
            if max1 == None or max1 < nums[i]:
                max2 = max1
                max1 = nums[i]
                max1index = i
            elif max2 < nums[i]:
                max2 = nums[i]
#        if max2 != None:        
#            print("max1 = %d , max2 = %d" %(max1, max2))
            
        if max2 != None and max1 >= 2*max2:
            return max1index
        elif max2 == None:
            return 0
        else:
            return -1