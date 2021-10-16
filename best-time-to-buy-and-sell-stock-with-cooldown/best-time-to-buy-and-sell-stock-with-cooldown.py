// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0
    
        buy = [0]*n
        sell = [0]*n
        cool = [0]*n
        buy[0] = -prices[0]
    
        for i in range(1, n):
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
            cool[i] = max(cool[i-1], sell[i-1])
      
        return sell[-1]  

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if not prices:
            return 0
        sold = 0
        rest = 0
        hold = -float('inf')
        for p in prices:
            psold = sold
            sold = hold+p
            hold=max(hold, rest-p)
            rest = max(rest, psold)
        return max(rest, sold)   
        
