import itertools
// https://leetcode.com/problems/24-game

class Solution:
    def judgePoint24(self, nums: 'List[int]') -> 'bool':
            if len(nums) == 1:
                return math.isclose(nums[0], 24)
            return any(self.judgePoint24([x] + rest)
                        for a, b, *rest in itertools.permutations(nums)
                        for x in {a+b, a-b, a*b, b and a/b})
        