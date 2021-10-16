// https://leetcode.com/problems/k-closest-points-to-origin

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        hp = [0]
        d = collections.defaultdict(list)
        for p in points:
            dst = p[0]*p[0]+p[1]*p[1]
            if len(hp) <= K:
                heapq.heappush(hp, -dst)
                d[dst]+=[p]
            else:
                val = -hp[0]
                if  dst < val:
                    if len(d[val]) > 0:
                        d[val].pop()
                    heapq.heappop(hp)
                    heapq.heappush(hp, -dst)
                    d[dst]+=[p]
        out = list()
        for k in d:
             if len(d[k]) > 0:
                out += d[k] 
        return out        
                    