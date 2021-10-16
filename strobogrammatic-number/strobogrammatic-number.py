// https://leetcode.com/problems/strobogrammatic-number

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d={'0':'0', '1':'1', '2':'E', '3':'S', '4':'H','5':'A', '6':'9', '7':'V', '8':'8', '9':'6' }
        out=''
        for ch in num:
            out=d[ch]+out
        return out == num    