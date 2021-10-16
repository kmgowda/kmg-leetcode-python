// https://leetcode.com/problems/guess-number-higher-or-lower-ii

class Solution(object):
    def getMoneyAmount1(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for l in range(n, 0, -1):
            for h in range(l+1, n+1):
                dp[l][h] = min(i + max(dp[l][i-1], dp[i+1][h])
                                    for i in range(l, h))
        return dp[1][n]
    
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem={}
        
        def calculate(l,h):
            if l >= h:
                return 0
            if (l,h) in mem:
                return mem[l,h]
            res = float('inf')
            for i in range((l+h)>>1, h+1):
                res = min(res,i+max(calculate(i+1, h), calculate(l, i-1)))
            mem[l,h]=res
            return res
        
        return calculate(1,n)