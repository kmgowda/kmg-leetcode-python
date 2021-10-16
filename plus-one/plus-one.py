// https://leetcode.com/problems/plus-one

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        for i in range(len(digits)-1, -1, -1):
            digits[i]+= 1
            if digits[i] > 9:
                digits[i] %=10
                last = True
            else:
                last = False
                break
        if last:
            res = [0]*(len(digits)+1)
            res[0]=1
            res[1:]=digits[:]
            return res
        else:
            return digits        