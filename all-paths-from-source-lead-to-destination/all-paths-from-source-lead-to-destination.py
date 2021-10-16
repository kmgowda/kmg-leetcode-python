// https://leetcode.com/problems/all-paths-from-source-lead-to-destination

class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        visited = collections.defaultdict(int)
        graph= collections.defaultdict(list)
        for [x,y] in edges:
            graph[x]+=[y]
                
        def dfs(node):
            if visited[node] == 1:
                return True
            elif visited[node] == -1:
                return False
            elif len(graph[node]) == 0:
                return node==destination
            else:
                visited[node] = -1
                for child in graph[node]:
                    if not dfs(child):
                        return False
                visited[node] = 1
                return True
        return dfs(source) 