// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = len(matrix)-1
        if i == -1:
            return False
        n = len(matrix[0])
        j = 0
        while i >= 0 and j < n:
            if matrix[i][j] > target:
                i-=1
            elif matrix[i][j] < target:
                j+=1
            else:
                return True
        return False    
        
        
                
        
        