// https://leetcode.com/problems/implement-rand10-using-rand7

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        idx = float('inf')
        while idx >  40:
            r = rand7()
            c = rand7()
            idx = r+(c-1)*7
        return 1 + (idx - 1) % 10     