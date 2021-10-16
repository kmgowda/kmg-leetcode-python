// https://leetcode.com/problems/implement-strstr

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl = len(needle)-1
        for i in range(len(haystack)-nl):
            l = nl
            while l >= 0:
                if haystack[i+l]!=needle[l]:
                    break
                l-=1    
            if l ==-1:
                return i
        return -1    
                