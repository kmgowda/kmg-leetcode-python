// https://leetcode.com/problems/largest-number

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
             return int(str(a)+str(b)) > int(str(b)+str(a))
            
        
        for i in range(1,len(nums)):
            for j in range(len(nums)-i):
                if not compare(nums[j],nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return str(int(''.join(map(str,nums))))
    
  
        