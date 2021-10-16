// https://leetcode.com/problems/range-sum-query-2d-mutable

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.mat = matrix
        self.m = len(matrix)
        if self.m > 0:
            self.n = len(matrix[0])
        else:
            self.n = 0
        

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.mat[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret=0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                ret+=self.mat[i][j]
        return ret        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)