// https://leetcode.com/problems/next-greater-element-i

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for i, x in enumerate(nums):
            d[x]=i
        
        ret = [-1]*len(findNums)
        for j, x in enumerate(findNums):
            i = d[x]+1
            while i < len(nums) and nums[i] < x:
                i+=1
            if i < len(nums) and nums[i] > x:    
                ret[j] = nums[i] 
        return ret    
                