// https://leetcode.com/problems/squares-of-a-sorted-array

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        arr=A[:]
        for i in range(len(arr)):
            arr[i]*=arr[i]
        arr.sort()
        return arr
            