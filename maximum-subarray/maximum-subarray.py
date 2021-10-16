// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        c_sum=0
        m_sum = -float('inf')
        for val in nums:
            if c_sum < 0:
                c_sum = 0
            c_sum+=val
            m_sum=max(m_sum, c_sum)
        return m_sum    