// https://leetcode.com/problems/minimum-window-subsequence

class Solution(object):
    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        m,n = len(S), len(T)
        dp = [[float('inf')]*(m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if S[j-1] == T[i-1]:
                    if i == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = dp[i][j-1]+1
        res = min(dp[-1])
        if res == float('inf'):return ''
        for i in range(1,m+1):
            if dp[-1][i] == res:
                return S[i-res:i]          