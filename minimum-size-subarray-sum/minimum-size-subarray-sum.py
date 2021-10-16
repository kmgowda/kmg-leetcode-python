// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        mincnt = 0
        i = 0
        left = 0
        for i , item in enumerate(nums):
            t+=item
            while t >= s:
                if mincnt == 0 or mincnt > (i+1-left):
                        mincnt = i+1-left
                t-=nums[left]
                left+=1
        return mincnt        
        