// https://leetcode.com/problems/maximize-distance-to-closest-person

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        pos, ans = -1, 0
        for i in range(len(seats)):
            if seats[i]:
                ans = max(ans, i if pos == -1 else (i-pos)//2)
                pos = i
        return max(ans, len(seats)-pos-1)        