// https://leetcode.com/problems/shortest-way-to-form-string

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        p, cnt  = -1,1
        
        for c in target:
            np = source.find(c, p+1)
            if np == -1:
               cnt+=1
               np = source.find(c)
               if np == -1:
                    return -1
            p = np
        return cnt    