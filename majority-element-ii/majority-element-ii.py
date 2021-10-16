// https://leetcode.com/problems/majority-element-ii

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnt=collections.Counter(nums)
        return [k for k in cnt if cnt[k] > len(nums)/3]        