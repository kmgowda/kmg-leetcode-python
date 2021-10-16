// https://leetcode.com/problems/shortest-palindrome

class Solution(object):
 
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_s = s[::-1]
        result = ""
        if (s == rev_s):
            return rev_s
        else:
            l = len(s)
            i = 1
            while(rev_s[i:] != s[:l-i]):
                i += 1            
            return rev_s[:i]+s
        