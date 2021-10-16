// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        count = n
        parent = range(n)
        
        def find(x):
            while parent[x] != x:
                 parent[x] = parent[parent[x]] # path compression
                 x = parent[x]
            return x
        
        for x,y in edges:
            x,y = find(x), find(y)
            if x != y:
                parent[x] = y
                count -= 1
        return count
            