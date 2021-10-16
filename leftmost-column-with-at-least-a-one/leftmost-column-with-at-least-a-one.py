// https://leetcode.com/problems/leftmost-column-with-at-least-a-one

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        N, M = binaryMatrix.dimensions()
        x = 0
        y = M-1
        while x < N and y >= 0:
            #print("x=%d, y=%d" %(x, y))
            if binaryMatrix.get(x, y):
                y-=1
            else:
                x+=1
                
        return y+1 if y < M-1 else -1        
 