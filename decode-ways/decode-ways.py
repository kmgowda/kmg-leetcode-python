// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0]=='0':
            return 0
        a, b = 1,1
        for i in range(1, len(s)):
            if s[i]=='0':
                if s[i-1]=='0' or s[i-1] > '2':
                    return 0
                else:
                    a, b = b,a
            else:
                if '10' < s[i-1:i+1] <= "26":
                    a, b = a+b, a
                else:
                    b = a
        return a         
            
        