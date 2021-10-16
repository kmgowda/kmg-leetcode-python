// https://leetcode.com/problems/all-paths-from-source-to-target

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def find(g, s, t, res,path):
            if s ==t:
                res.append(path[:])
                return
            for v in g[s]:
                find(g, v, t,res, path+[v])
        res=[]
        find(graph,0,len(graph)-1,res,[0])
        return res