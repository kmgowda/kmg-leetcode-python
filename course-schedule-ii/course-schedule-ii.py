// https://leetcode.com/problems/course-schedule-ii

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        g = [[] for _ in range(numCourses)]
        vis=[0]*numCourses
        ret = list()
        
        for i,j in prerequisites:
            g[i].append(j)
        
        for i in range(numCourses):
            if not self.dfs(g, vis, ret, i):
                return []
        return ret
    
    def dfs(self, g, v, r, i):
        if v[i] == -1: return False
        if v[i] == 1: return True
        v[i] = -1
        for j in g[i]:
            if not self.dfs(g, v, r, j):
                return False
        v[i] = 1
        r.append(i)
        return True
        