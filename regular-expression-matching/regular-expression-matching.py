// https://leetcode.com/problems/regular-expression-matching

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        DP = [[False]*(n+1) for i in range(m+1)]
        DP[0][0] = True 
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1] == '*':
                    DP[i][j] = DP[i][j-2] or (i > 0 and j > 1 and (p[j-2] == '.' or s[i-1] == p[j-2]) and DP[i-1][j])
                elif i > 0 and (p[j-1] == '.' or p[j-1] == s[i-1]):
                    DP[i][j] = DP[i-1][j-1] 
        return DP[m][n]    