// https://leetcode.com/problems/wildcard-matching

class Solution(object):
    
    def ismatch_rec(self, s, p):
        if not len(p) and len(s):
            return False
        if not len(s):
            if not len(p):
                return True
            elif p[0]=='*':
                return self.ismatch_rec(s, p[1:])
            else:
                return False
        if p[0] == '*':
            if not self.ismatch_rec(s[1:], p):
               if not self.ismatch_rec(s[1:], p[1:]):
                  return self.ismatch_rec(s, p[1:])
               else:
                return True
            else:
                return True
        elif p[0] == '?' or s[0] == p[0]:
            return self.ismatch_rec(s[1:],p[1:])
        else:
            return False
    
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i,j,s_star,p_star = 0,0,0,-1
        while i<len(s):
            if j<len(p) and (s[i]==p[j] or p[j]=='?'):
                i,j = i+1,j+1
            elif j<len(p) and p[j]=='*':
                s_star,p_star = i,j
                j+=1
            elif p_star!=-1:
                s_star +=1
                i,j = s_star,p_star+1
            else:
                return False
        
        while j<len(p) and p[j]=='*':
            j+=1
        return True if j==len(p) else False
   
        