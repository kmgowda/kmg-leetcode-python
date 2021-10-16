// https://leetcode.com/problems/last-stone-weight

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        h = []
        for x in stones:
            heapq.heappush(h, -x)
        while h:
            x = heapq.heappop(h)*-1
            if not h:
                return x
            y = heapq.heappop(h)*-1
            #val = (x-y)*-1
            #print("x=%d, y=%d, val=%d\n" %(x,y, val))
            heapq.heappush(h, -(x-y))
        return None    