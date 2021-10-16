// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x:
            r = r*10+x%10
            x//=10
        
        r= r*sign
        if sign ==-1:
            if r < -1*2**31:
                return 0
        elif r >  2**31 - 1:
                return 0
        return r    
        
            
