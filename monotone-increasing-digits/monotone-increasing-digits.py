// https://leetcode.com/problems/monotone-increasing-digits

class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
       # get every digits in N
        digits = map(int, list(str(N)))
        
        l = len(digits)
        
        # find the first digit, that is not monotone
        i = 1
        while i < l and digits[i - 1] <= digits[i]:
            i += 1
        
        # if all digits are monotone, return N
        if i == l:
            # print i, l, N
            return N
        
        # find the first one that is great than the previous digit plus one
        while i > 0 and digits[i] - 1 < digits[i - 1]:
            i -= 1
        
        digits[i] -= 1
        # all digits after i's position should be 9
        res = 0
        for j in range(l):
            res *= 10
            if j > i:
                res += 9
            else:
                res += digits[j]
        
        return res        