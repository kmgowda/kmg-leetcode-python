// https://leetcode.com/problems/reverse-string

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=[0]*len(s)
        
        i = 0
        j = len(s)-1
        
        while i<=j:
            ret[i]=s[j]
            ret[j]=s[i]
            i+=1
            j-=1
        return "".join(ret)
