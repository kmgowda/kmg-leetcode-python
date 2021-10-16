// https://leetcode.com/problems/container-with-most-water

class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mp = 0
        for i in range(1, len(height)):
             for j in range(0, i):
                   m = min(height[j] , height[i])
                   p =(i-j)*m
                   mp = max(mp,p)
        return mp
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        R = len(height)-1
        L = 0
        ret = 0
        while L != R:
            ret = max(ret, min(height[L], height[R])*(R-L))
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1                
        return ret