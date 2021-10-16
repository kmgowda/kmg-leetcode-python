// https://leetcode.com/problems/the-skyline-problem

from collections import defaultdict
from heapq import heappush, heappop

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return buildings
        
        # Critical points where we use negative heights for building's left points
        points = []
        for l, r, h in buildings:
            points += [(l, -h), (r, h)]
            
        #print("Before")
        #print(points)
        # Sort critical points where two points have the same x-corrdinates 
        # will be sorted based on whether they are left or right points.
        points.sort()
        #print("After")
        #print(points)
        
        # Use a heap to store heights where the last height is 0 
        # and other elements are negative
        result = []
        heights = [0]
        prev = heights[0]
				
        # Save the heights that will be removed later
        ignored = defaultdict(int)
        
        for x, h in points:
            if h < 0:
                heappush(heights, h)
            else:
                ignored[-h] += 1

            # Remove heights if they become the root of the heap
            while ignored[heights[0]] > 0:
                ignored[heights[0]] -= 1
                heappop(heights)

            # The first element is value of the heap's root node                
            cur = heights[0]
            if cur != prev:
                result.append((x, -cur))
                prev = cur
        
        return result