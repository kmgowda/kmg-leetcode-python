// https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L, R = 1, n
        while L <= R:
            mid = L + ((R - L) >> 1)
            res = guess(mid)
            #print("mid : %d, guess = %d , input n: %d" %(mid,res, n))
            if res == 0:
                return mid
            elif res == 1:
                L = mid + 1
            else:
                R = mid - 1
        return L        