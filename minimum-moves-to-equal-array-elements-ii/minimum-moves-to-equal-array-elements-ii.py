// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=sorted(nums)
        m = len(arr)>>1
        cnt=0
        for a in arr[:m]:
            cnt+=arr[m]-a
        for a in arr[m+1:]:
            cnt+=a-arr[m]
        return cnt    