// https://leetcode.com/problems/valid-palindrome-ii

class Solution:
    
    def is_palindrome(self, s):
        l = 0
        h = len(s)-1
        while l < h:
            if s[l] != s[h]:
                return (l, h)
            l+=1
            h-=1
        return (0, 0)
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, h = self.is_palindrome(s)
        if not h:
            return True
        l, h1 = self.is_palindrome(s[:l]+s[l+1:])
        if h1:
            l, h = self.is_palindrome(s[:h]+s[h+1:])
            if h:
                return False
        return True    
        