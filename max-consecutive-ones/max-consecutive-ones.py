// https://leetcode.com/problems/max-consecutive-ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        for item in nums:
            if item == 1:
                one+=1
            else:
              if two < one:
                two = one
              one = 0
        if two < one:
            two = one
        return two    