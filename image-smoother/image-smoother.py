// https://leetcode.com/problems/image-smoother

from math import floor

class Solution:
    
    def inRange(self, arr, i, j):
        return i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0])
    
    def neighborAverage(self, arr, i, j):
        dirs = [(-1, -1), (0, -1), (1, -1),
                (-1, 0), (0, 0), (1, 0),
                (-1, 1), (0, 1), (1, 1)]
        value, count = 0, 0
        for item in dirs:
            x, y = item
            if(self.inRange(arr, x + i, y + j)):
                value += arr[x + i][y + j]
                count += 1
        return int(floor(value / count))
            
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[0 for i in range(len(M[0]))] for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                ret[i][j] = self.neighborAverage(M, i, j)
        return ret