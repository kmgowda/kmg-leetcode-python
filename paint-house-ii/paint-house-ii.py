// https://leetcode.com/problems/paint-house-ii

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in range(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1]) 