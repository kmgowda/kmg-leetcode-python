// https://leetcode.com/problems/power-of-three

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        return 1162261467%n == 0