// https://leetcode.com/problems/unique-paths-iii

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        N = len(grid[0])
        self.res=0
        
        def walk(grid, i, j, M, N, vis, left):
            if grid[i][j]==2 and left == 0:
                self.res+=1
                return
            for (x, y) in [(i+1, j), (i-1, j),(i,j+1),(i,j-1)]:
                if 0<=x<M and 0<=y<N and not vis[x][y] and grid[x][y] != -1:
                        vis[x][y] = True
                        walk(grid, x, y, M, N,vis, left-(grid[x][y]==0) )  
                        vis[x][y] = False  
        
        vis=[[False]*N for _ in range(M)]
        left=0 
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    start=(i,j)
                if grid[i][j] == 0:
                    left+=1
        i,j=start            
        vis[i][j]=True
        walk(grid, i,j, M,N, vis, left)
        return self.res
    
    
