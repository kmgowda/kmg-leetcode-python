// https://leetcode.com/problems/sum-of-two-integers

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # 32 bits integer max
        MAX = 0x7FFFFFFF
 
        # mask to get last 32 bits
        MASK = 0xFFFFFFFF
        s, c = a, b
        while b:
            s = (a^b)&MASK
            c = ((a&b)<<1)&MASK
            a, b = s, c
       
        return s if s <= MAX else ~(s ^ MASK)