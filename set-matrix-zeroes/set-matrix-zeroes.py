// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows=[False]*R
        cols=[False]*C
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True
        for i in range(R):
             for j in range(C):
                    if rows[i] or cols[j]:
                        matrix[i][j]=0

                    