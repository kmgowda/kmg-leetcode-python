// https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lt = s.split()
        st =""
        for word in lt:
            st +=" "+word[::-1]
        return st[1:]    
        