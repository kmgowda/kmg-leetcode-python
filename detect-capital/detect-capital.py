// https://leetcode.com/problems/detect-capital

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cnt = 0
        pos = 0
        for i, c in enumerate(word):
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                cnt+=1
                pos = i
        
        if cnt == 1:
            if pos:
                return False
        if 1 < cnt < len(word):
               return False
        
        return True    
                