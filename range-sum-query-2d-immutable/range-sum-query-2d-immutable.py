// https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.M = len(matrix)
        self.N = len(matrix[0]) if self.M > 0 else 0
        self.dp = [[0]*(self.N+1) for _ in range(self.M+1)]
        
        for i in range(1, self.M+1):
            for j in range(1, self.N+1):
                self.dp[i][j] = self.dp[i-1][j]+ self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]
  
           

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1] -self.dp[row2+1][col1] + self.dp[row1][col1] 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)