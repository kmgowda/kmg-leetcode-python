// https://leetcode.com/problems/longest-consecutive-sequence

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d= collections.Counter(nums)
        ma = 0
        for k in d:
            j = k
            if d[j-1]: 
                continue
            count=0
            while d[j]:
                j+=1
                count+=1
            ma = max(ma, count)
        return ma    