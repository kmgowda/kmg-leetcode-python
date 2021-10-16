// https://leetcode.com/problems/reverse-words-in-a-string

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lt = s.split()
        st = ""
        for word in lt:
            st= word+" "+st
        return st[:-1]    
        