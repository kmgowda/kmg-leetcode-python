// https://leetcode.com/problems/pascals-triangle-ii

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
                
        if not rowIndex:
            return [1]
        ret = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
#            print(ret)
            prev = ret[0]
            for j in range(1, i):
                tmp = ret[j]
                ret[j] += prev
                prev = tmp
        return ret        
                
        
        
        