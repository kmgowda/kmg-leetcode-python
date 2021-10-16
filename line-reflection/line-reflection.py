// https://leetcode.com/problems/line-reflection

class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        xmax, xmin = float('-inf'), float('inf')
        points_set = set()
        for x,y in points:
            xmax = max(xmax,x)
            xmin = min(xmin, x)
            points_set.add((x, y))
        total = xmin + xmax
        for x,y in points:
            if (total-x,y) not in points_set:
                return False
        return True
        