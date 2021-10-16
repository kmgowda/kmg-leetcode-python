// https://leetcode.com/problems/sparse-matrix-multiplication

class Solution(object):
    def multiply1(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
  
        mat = [[0]*len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    mat[i][j] += A[i][k] * B[k][j]
                    print("(%d,%d) += (%d, %d)*(%d, %d)" %(i, j, i, k, k, j))
        return mat 
    
    
    

    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        R = [[0] * len(B[0])  for __ in range(0,len(A))]
        htA = [dict() for _ in range(len(A))]
        htB = [dict() for _ in range(len(B))]

        for row in range(len(B)):
            for col in range(len(B[0])):
                if B[row][col]:
                    htB[row][col] = B[row][col]
        for row in range(len(A)):
            for col in range(len(A[0])):
                if A[row][col]:
                    htA[row][col] = A[row][col]
        for row in range(len(A)):
            for col in range(len(B[0])):
                for k in htA[row]:
                    if col in htB[k]:
                        R[row][col]+=htA[row][k]*htB[k][col]
        return R
    
 
    