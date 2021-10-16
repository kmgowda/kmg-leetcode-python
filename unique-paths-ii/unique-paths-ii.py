// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        dp = [[1]*N for _ in range(M)]
        
         
        for i in range(0, M):
            for j in range(0, N):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j]=dp[i][j-1]
                elif j == 0:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]            
                    
        