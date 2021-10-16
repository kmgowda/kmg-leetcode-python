// https://leetcode.com/problems/missing-number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        n = len(nums)
        s1 = (n*(n+1))//2
        return s1-s