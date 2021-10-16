// https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        
        cnt=0
        for i in range(M):
            for j in range(N):
                if not grid[i][j]: continue
                cnt+=4
                for (k,l) in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                    if 0<=k<M and 0<=l<N and grid[k][l]:
                        cnt-=1
        return cnt 
            
  