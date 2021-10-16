// https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        d = collections.Counter(s)
        for c in t:
            if d[c] < 1:
                return False
            d[c]-=1
        return True    