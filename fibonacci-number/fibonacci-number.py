// https://leetcode.com/problems/fibonacci-number

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        d= collections.defaultdict(int)
        
        def get(n):
            if n==0:
                return 0
            if n== 1:
                return 1
            if d[n]:
                return d[n]
            d[n]=get(n-1)+get(n-2)
            return d[n]
        
        return get(N)