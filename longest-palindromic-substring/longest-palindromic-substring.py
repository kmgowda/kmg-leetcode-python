// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    
    def is_palindrome(self, s, l, h):
        while l < h:
            if s[l] != s[h]:
                return False
            l+=1
            h-=1
        return True    
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        
        if N <= 1:
            return s
        
        l = 0
        h = 0
        for i in range(N):
            for j in range(N-1, i, -1):
                if s[i] == s[j] and j-i > h-l and self.is_palindrome(s, i, j):
                    l = i
                    h = j
                    break
        st = s[l:h+1]
        return st
        
                    
        