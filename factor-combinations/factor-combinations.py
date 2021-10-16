// https://leetcode.com/problems/factor-combinations

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = []
        def dfs(cur, i):
            num = cur.pop()
            while i*i <= num:
                div = num/i
                if num%i==0:
                    ret.append(cur+[i, div])
                    dfs(cur+[i, div], i)
                i+=1
        dfs([n], 2)
        return ret        