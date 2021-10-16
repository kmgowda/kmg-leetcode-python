// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        mp = prices[0]
        s = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                s+=(prices[i-1]-mp)
                mp= prices[i]
            else:
                mp = min(mp, prices[i])
        s+=prices[-1]-mp        
        return s         
                    