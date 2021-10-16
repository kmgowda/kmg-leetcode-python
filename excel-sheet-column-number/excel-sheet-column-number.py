// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        b = 1
        su = 0
        for i in range(len(s)-1, -1, -1):
            su+=b*(ord(s[i])-ord('A')+1)
            b*=26
        return su    