// https://leetcode.com/problems/climbing-stairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        d= collections.defaultdict(int)
        
        def climb(s):
            if s <= 0:
                return 1
            if s ==1:
                return 1
            if d[s]:
                return d[s]
            d[s]=climb(s-1)+climb(s-2)
            return d[s]
        
        return climb(n)
            