// https://leetcode.com/problems/peak-index-in-a-mountain-array

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, h = 0, len(A) - 1
        while l < h:
            mi = (l + h) >>1
            if A[mi] < A[mi + 1]:
                l = mi + 1
            else:
                h = mi
        return l