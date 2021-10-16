// https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map1={}
        map2={}
        for i in range(len(s)):
            if s[i] in map1:
                if map1[s[i]] != t[i]:
                    return False
            if t[i] in map2:
                if map2[t[i]] != s[i]:
                    return False
            map1[s[i]] = t[i]
            map2[t[i]] = s[i]
                
        return True        
        