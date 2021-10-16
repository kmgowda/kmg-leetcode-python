// https://leetcode.com/problems/multiply-strings

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def atoi(s):
            n=0
            for c in s:
                n=n*10+(ord(c)-ord('0'))
            return n
        
        def itoa(n):
            if not n:
                return "0"
            s=""
            while n:
                c=ord('0')+n%10
                s=chr(c)+s
                n//=10
            return s
        
        return itoa(atoi(num1)*atoi(num2))
                