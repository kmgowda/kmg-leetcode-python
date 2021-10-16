// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        one, two , three = -float('inf'), -float('inf'), -float('inf')
 
        for n in nums:
            if one <= n:
                if one < n:
                    three = two
                    two = one
                one = n
            elif two <= n:
                 if two < n:
                        three = two
                 two = n
            elif three < n:
                three = n
        return three if three != -float('inf') else max(one, two)        
        