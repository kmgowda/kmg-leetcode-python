// https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        ret = None
        for key in nums:
            if key in hash:
                hash[key]+=1
            else:
                hash[key]=1
       
        for key in hash.keys():
            if hash[key] == 1:
                return key
        return ret        
        