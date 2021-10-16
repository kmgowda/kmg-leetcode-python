// https://leetcode.com/problems/target-sum

from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1
        for x in nums:
            step = defaultdict(int)
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
            #print(count)

        return count[S]        