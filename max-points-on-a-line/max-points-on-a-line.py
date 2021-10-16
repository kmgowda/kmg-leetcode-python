// https://leetcode.com/problems/max-points-on-a-line

# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import numpy
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        m = 0
        for i in range(l):
            d = {'k':1}
            same = 0
            x1 = points[i].x
            y1 = points[i].y
            for j in range(i+1, l):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2 and y1 == y2: 
                    same+=1
                    continue
                    
                if x1 == x2:
                    slope='k'
                else:    
                    slope = ((y1-y2)* numpy.longdouble(1)) /(x1-x2)
                if slope not in d: 
                    d[slope] = 1
                d[slope] += 1
            m = max(m, max(d.values())+same) 
        return m        