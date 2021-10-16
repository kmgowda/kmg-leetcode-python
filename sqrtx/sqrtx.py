// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        left = 0
        right = x
        g = (left+right)/2
        diff = abs(g**2-x)
        while diff > 0.001 and diff < x**2:
             if g**2 < x:
                left = g
             else:
                right = g
             g = (left+right)/2
             diff = abs(g**2-x)
 
            
        return (int(g))