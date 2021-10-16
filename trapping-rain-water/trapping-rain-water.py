// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N= len(height)
        if N < 2:
            return 0
        i = N-1
        for i in range(N-1):
            if height[i] > height[i+1]:
                break
        start = i
        h = i
        total = 0
        unit = 0
        for i in range(start+1, N):
            if height[i] < height[h]:
                unit+=height[h]-height[i]
            else:
                h = i
                total+=unit
                unit = 0
        for i in range(N-1, h, -1):
            if height[i] > height[i-1]:
                break
        start = i
        e = h
        h = start
        unit = 0
        for i in range(start, e-1, -1):
            if height[i] < height[h]:
                unit+=height[h]-height[i]
            else:
                h = i
                total+=unit
                unit = 0            

        return total        