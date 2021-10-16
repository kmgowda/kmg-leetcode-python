// https://leetcode.com/problems/first-missing-positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi = None
        ma = None
        for n in nums:
            if (mi == None and n > 0) or (mi != None and n < mi and n > 0) :
                mi = n
            if (ma == None and n > 0) or (ma != None and n > ma and n > 0) :
                ma = n
        if not mi and not ma: return 1
        for i in range(1, mi):
            if i not in nums:
                return i
 
        for i in range(mi+1, ma):
            if i not in nums:
                return i
        return ma+1    
                