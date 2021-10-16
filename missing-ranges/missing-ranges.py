// https://leetcode.com/problems/missing-ranges

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        l = lower
        ret = list()

        if len(nums) == 0:
            st = str(lower)
            if l < upper:
                st+="->"+str(upper)
            ret.append(st)
            return ret
            
        for i in range(len(nums)):
            u = nums[i]-1
            if l <= u < upper:
                 st = str(l)
                 if l < u:
                    st+="->"+str(u)
                 ret.append(st)
            l = nums[i]+1
        
        if nums[-1]+1 <= upper:
            st = str(nums[-1]+1)
            if nums[-1]+1 < upper:
                st+="->"+str(upper)
            ret.append(st)  
        return ret    
                
        