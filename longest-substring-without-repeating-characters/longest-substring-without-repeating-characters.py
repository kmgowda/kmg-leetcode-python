// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map={}
        curlen = 0
        maxlen = 0
        for i, ch in enumerate(s):
            if ch not in map:
                map[ch]= i
                prev = -1
            else:
                prev = map[ch]
                map[ch] = i
            if prev == -1 or i-curlen > prev:
                curlen+=1
            else:
                if maxlen < curlen:
                    maxlen = curlen
                curlen = i-prev
        if maxlen < curlen:
            maxlen = curlen
        return maxlen    
                
 