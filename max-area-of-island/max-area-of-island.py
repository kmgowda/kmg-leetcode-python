// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        
        
        def getarea(i, j, M, N, vis):
            ret = 0
            if 0<=i<M and 0<=j<N and grid[i][j] and not vis[i][j]:
                 vis[i][j] = True
                 ret = (getarea(i-1,j,M,N, vis) + 
                              getarea(i+1,j,M,N, vis) +  
                              getarea(i,j-1,M,N, vis) +  
                              getarea(i,j+1,M,N, vis)+ 1)
                #vis[i][j]=False
            return ret
        
        M = len(grid)
        N = len(grid[0])
        vis = [[False]*N for _ in range(M)]
        ma = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                   ma = max(ma, getarea(i,j,M,N,vis))
        return ma            
                    
                    
            