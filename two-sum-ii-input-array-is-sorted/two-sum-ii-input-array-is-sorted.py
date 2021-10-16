// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution(object):
  
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, h = 0, len(numbers)-1
        
        while l< h:
              x = numbers[l]+numbers[h]
              if x < target:
                l+=1
              elif x > target:
                h-=1
              else:
                return [l+1, h+1]
        return [-1,-1]        