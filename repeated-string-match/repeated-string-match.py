// https://leetcode.com/problems/repeated-string-match

class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        a = len(A)
        b = len(B)
        tmp=""
        c = 0
        while len(tmp) < b:
            tmp+=A
            c+=1
        if B in tmp:
            return c
        tmp+=A
        c+=1
        if B in tmp:
            return c
       
        return -1        
                
        