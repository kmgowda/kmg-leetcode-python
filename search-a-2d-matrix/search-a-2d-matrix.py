// https://leetcode.com/problems/search-a-2d-matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix):
            return False
        r = 0
        for i in range(len(matrix)):
            if len(matrix[i]) > 0 and  matrix[i][0] <= target and target <= matrix[i][-1]: 
                r = i
                break
        return True if target in matrix[r] else False
            
        