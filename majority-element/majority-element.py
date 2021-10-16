// https://leetcode.com/problems/majority-element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        for k in d:
            if d[k] > (len(nums)//2):
                return k
        return -1    