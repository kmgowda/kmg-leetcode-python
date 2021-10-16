// https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            d[n] += [i]
        for i, n in enumerate(nums):
             for j in d[target-n]:
                if i != j:
                    return (i, j)
        return (-1, -1) 