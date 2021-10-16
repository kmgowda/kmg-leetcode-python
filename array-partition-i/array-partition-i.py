// https://leetcode.com/problems/array-partition-i

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        s = 0
        for i in range(0, len(nums), 2):
            if nums[i] < nums[i+1]:
                s+=nums[i]
            else:
                s+=nums[i+1]
        return s 