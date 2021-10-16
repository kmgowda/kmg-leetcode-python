// https://leetcode.com/problems/find-pivot-index

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_l, sum_r =  0, sum(nums)

        for idx in range(0, len(nums)):
            sum_l = sum_l + nums[idx]
            if sum_l == sum_r:
                return idx
            sum_r = sum_r - nums[idx]
        return -1