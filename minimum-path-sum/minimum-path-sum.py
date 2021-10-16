// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def pathsum(i,j):
            if i < M and j < N:
                r=pathsum(i,j+1)
                b=pathsum(i+1,j)
                #print("(%d, %d)  r = %d, b=%d" %(i,j, r, b))
                
                if r == -1 and b == -1:
                    return grid[i][j]
                elif r == -1:
                    return  grid[i][j]+b
                elif b == -1:
                    return grid[i][j]+r
                elif r < b:
                    return grid[i][j]+r
                else:
                    return grid[i][j]+b
            else:
                return -1
                    
 
            
        M = len(grid)
        N = len(grid[0])
        return pathsum(0,0)
    
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """    
        M = len(grid)
        N = len(grid[0])
        dp =[[float('inf')]*N for _ in range(M)]
        q = collections.deque()
        q.append((0,0))
        dp[0][0] = grid[0][0]
        while q:
           (k, l) = q.pop()
           for (i, j) in [(k+1, l), (k, l+1)]:
                if i < M and j < N:
                    t =  dp[k][l]+grid[i][j]
                    if t < dp[i][j]:
                        dp[i][j] = t
                        q.append((i, j))
        return dp[M-1][N-1]     
    
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(i == 0 and j > 0):
                    grid[i][j] +=  grid[i][j-1]
                elif(j == 0 and i > 0):
                    grid[i][j] += grid[i-1][j]
                elif(i > 0 and j > 0):
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
                    
        return grid[i][j]
                    
    