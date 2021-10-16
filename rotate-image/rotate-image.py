// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i, N):
                #print("swapping : %d & %d" %(matrix[i][j], matrix[j][N-1-i]))
                tmp = matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=tmp
                
        col = N//2
        if N&1:
             col+=1
        for i in range(N):
            for j in range(col):
                 tmp = matrix[i][j]
                 matrix[i][j] = matrix[i][N-1-j]
                 matrix[i][N-1-j] = tmp 
         
            