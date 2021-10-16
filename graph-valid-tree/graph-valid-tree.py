// https://leetcode.com/problems/graph-valid-tree

from collections import defaultdict, deque

class Solution:
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n != len(edges) + 1:
            return False
        
        adjList = defaultdict(list)
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        vis = set([])
        q = deque()
        q.append(0)
        parent = [-1 for _ in range(n)]
        
        while len(q) != 0:
            u = q.popleft()
            vis.add(u)
            
            for v in adjList[u]:
                if v in vis and parent[u] != v:
                    return False
                if v not in vis:
                    q.append(v)
                    parent[v] = u
        
        return len(vis) == n
                    
                
        
            