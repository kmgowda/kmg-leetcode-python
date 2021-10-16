// https://leetcode.com/problems/add-strings

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def atoi(s):
            ret=0
            for c in s:
                ret=ret*10+ord(c)-ord('0')
            return ret
        
        def itoa(n):
            if n == 0:
                return '0'
            
            s=''
            while n:
                s=str(n%10)+s
                n=n//10
            return s
        
        return itoa(atoi(num1)+atoi(num2))
                