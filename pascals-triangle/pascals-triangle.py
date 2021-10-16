// https://leetcode.com/problems/pascals-triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return list()
        ret = list()
        tmp = [1]
        ret.append(tmp)
        for i in range(numRows-1):
            h = len(ret[i])
            tmp = [0]*(h+1)
            tmp[0]= ret[i][0]
            tmp[h]= ret[i][h-1]
            l = 1
            h-=1
            while l <= h:
                tmp[l]=ret[i][l-1]+ret[i][l]
                tmp[h]=ret[i][h-1]+ret[i][h]
                l+=1
                h-=1
            ret.append(tmp)
        return ret        
                