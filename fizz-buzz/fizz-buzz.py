// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret=list()
        for i in range(1, n+1):
            if not i%3 and not i%5:
                ret.append("FizzBuzz")
            elif not i%3:
                ret.append("Fizz")
            elif not i%5:
                ret.append("Buzz")
            else:
                ret.append(str(i))
        return ret        