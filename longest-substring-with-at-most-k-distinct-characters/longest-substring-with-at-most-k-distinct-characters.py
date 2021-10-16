// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

class Solution(object):
    # TLE
    def lengthOfLongestSubstringKDistinct1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m = 0
        for i in range(len(s)):
            c = k
            sub=set()
            l = 0
            for j in range(i, len(s)):
                if s[j] in sub:
                    l+=1
                elif c > 0:
                    sub.add(s[j])
                    l+=1
                    c-=1
                else:
                    break
                   
            if l > m:
                m = l
        return m 

    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret    
    
    
    
    