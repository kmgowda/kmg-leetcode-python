// https://leetcode.com/problems/split-array-largest-sum

class Solution(object):
    
    def cansplit(self, a, maxval, sub):
        cnt = 1
        csum = 0
        for i in a:
            csum +=i
            if csum > maxval:
                csum = i
                cnt+=1
                if cnt > sub:
                    return False
        return True        
    
    
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if not len(nums):
            return 0
        l , h = None, 0
        for i in nums:
            if l == None or l < i:
                l = i
            h+=i
        if m == len(nums):
            return l
        if m == 1:
            return h
        while l < h:
            mid = (l+h)>>1
            if self.cansplit(nums, mid, m):
                h = mid
            else:
                l = mid+1
        return l        
        