// https://leetcode.com/problems/valid-perfect-square

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        s = 0
        i = 1
        while s < num:
            s +=i
            if s == num:
                return True
            i+=2
        return False    