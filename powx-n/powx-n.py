// https://leetcode.com/problems/powx-n

class Solution(object):
    def pow_rec(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        p = self.pow_rec(x,n//2)
        if n&1:
            return x*p*p
        return p*p
    
    
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n*=-1
        return self.pow_rec(x,n)    
 
            