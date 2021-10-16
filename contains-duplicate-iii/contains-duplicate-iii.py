// https://leetcode.com/problems/contains-duplicate-iii

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or not nums or k <= 0:
            return False
        buckets = {}
        width = t + 1

        for n, i in enumerate(nums):
            buck = i // width
            if buck in buckets:
                return True
            else:
                buckets[buck] = i
            if buck - 1 in buckets and i - buckets[buck-1] <= t:
                return True
            if buck + 1 in buckets and buckets[buck+1] - i <= t:
                return True
            if n >= k:
                del buckets[nums[n-k] // width]
        return False  