// https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
            # turn off rightmost 1-bit
            n = n & (n - 1)
        return m & n