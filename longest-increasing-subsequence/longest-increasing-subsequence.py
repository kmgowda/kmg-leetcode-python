// https://leetcode.com/problems/longest-increasing-subsequence

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        val = [1] * len(nums)
        i, j = 1, 0
        while i < len(nums):
            if j < i:
                if nums[j] < nums[i]:
                    val[i]=max(val[i], val[j]+1)
                j+=1
            else:
                i+=1
                j=0
        m = val[0]
        for i in val:
            m = max(m,i)
        return m    