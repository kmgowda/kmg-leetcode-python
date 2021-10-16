// https://leetcode.com/problems/evaluate-division

from collections import defaultdict, deque

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        lookup = defaultdict(dict)
        for i, eqn in enumerate(equations):
            v1, v2 = eqn
            lookup[v1][v2] = values[i]
            lookup[v2][v1] = 1/values[i]
        #print(lookup)    
            
        def _bfs(start, target):
            queue = deque([(start, 1.0)])
            seen = set()
            while queue:
                e, val = queue.popleft()
                seen.add(e)
                for k, v in lookup[e].items():
                    #print(e, k, v)
                    if k == target:
                        return val * v
                    elif k not in seen:
                        queue.append((k, val * v))
            return -1.0
        
        return [_bfs(*q) for q in queries]        