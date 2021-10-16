// https://leetcode.com/problems/fraction-to-recurring-decimal

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0: return str(numerator // denominator)
        p, q = map(abs, (numerator, denominator))
        prefix = ('' if (numerator > 0) == (denominator > 0) else '-') + str(p // q) + '.' # everything before the decimal point
        suffix = '' # everything after the decimal point
        r = p % q
        d = {}
        while r not in d: # search for recurrence
            d[r] = len(d)
            suffix += str(r * 10 // q)
            r = r * 10 % q
            if r == 0: return prefix + suffix # no recurring decimal
        return prefix + suffix[:d[r]] + '(' + suffix[d[r]:] + ')'