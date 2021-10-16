// https://leetcode.com/problems/maximal-square

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        r = len(matrix)
        c = len(matrix[0]) if r > 0 else 0
        dp = [0]*(c+1)
        maxl =  prv = 0
        for i in range(1, r+1):
            for j in range(1, c+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(min(dp[j-1], prv), dp[j])+1
                    maxl = max(maxl, dp[j])
                else:
                    dp[j] = 0
                prv = tmp
        return maxl*maxl        
                    