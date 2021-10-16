// https://leetcode.com/problems/perfect-squares

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [i*i  for i in range(1, int(math.sqrt(n))+1)]
        l = 0
        cur =set()
        cur.add(0)
        
        while True:
            nxt = set()
            for a in cur:
                for b in s:
                    if a+b == n:
                        return l+1
                    elif a+b < n:
                       nxt.add(a+b)
            cur = nxt
            l+=1
            
        