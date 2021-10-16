// https://leetcode.com/problems/palindrome-permutation

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d= collections.Counter(s)
        odd = 0
        for cnt in d.values():
            if cnt % 2:
                odd += 1
                if odd > 1:
                    return False
        
        return True
    
                
            