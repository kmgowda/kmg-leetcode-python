// https://leetcode.com/problems/diagonal-traverse

class Solution(object):
   
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        M = len(matrix)
        ret = list()
        if M == 0:
            return ret
        N = len(matrix[0])
        r = 0
        c = 0
      
        for i in range(M*N):
            ret.append(matrix[r][c])
            if (r+c)%2 == 0:
                if c == N-1:
                    r+=1
                elif r == 0:
                    c+=1
                else:
                    r -=1
                    c +=1
            else:
                if r == M-1:
                    c+=1
                elif c== 0:
                    r +=1
                else:
                    r+=1
                    c-=1
        return ret            

            
                