// https://leetcode.com/problems/1-bit-and-2-bit-characters

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits: 
            return False
        n = len(bits)
    
        idx = 0
        while idx < n:
            if idx == n-1 : 
                return True
            if bits[idx] == 1: 
                idx += 2              
            else: 
                idx += 1
        return False