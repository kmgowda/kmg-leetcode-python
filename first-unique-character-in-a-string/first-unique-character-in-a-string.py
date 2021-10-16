// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        d={}
        for i, ch in enumerate(s):
            if ch in d:
                d[ch]=len(s)
            else:
                d[ch] = i
        pos = min(d.values())
        if pos < len(s):
            return pos
        return -1
        