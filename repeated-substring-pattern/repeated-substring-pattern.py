// https://leetcode.com/problems/repeated-substring-pattern

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            ret = False
            for j in range(i+1, len(s), i+1):
                if s[:i+1] != s[j:j+i+1]:
                    ret = False
                    break
                else:
                    ret = True
            if ret:
                return True
        return False    
                    