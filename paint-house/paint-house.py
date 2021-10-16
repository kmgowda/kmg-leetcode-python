// https://leetcode.com/problems/paint-house

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        red, blue, green = 0, 0, 0
        for cr, cb, cg in costs:
            red, blue, green = min(blue, green) + cr, min(red, green) + cb, min(red, blue) + cg
        return min(red, blue, green)