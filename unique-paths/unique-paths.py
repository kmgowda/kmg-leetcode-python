// https://leetcode.com/problems/unique-paths

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d =[[1]*n for _ in range(m)]
        
       
        for i in range(1, m):
            for j in range(1, n):
                d[i][j]=d[i-1][j]+d[i][j-1]
        return d[-1][-1]        