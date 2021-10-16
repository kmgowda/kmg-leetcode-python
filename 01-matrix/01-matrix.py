// https://leetcode.com/problems/01-matrix

from collections import deque

class Solution:
    
    def update_rec(self, matrix, vis, r, c, R, C, val):
        if (r > -1 and c > -1 and r < R and c < C) and  ((matrix[r][c] > val and vis[r][c]) or (not vis[r][c])):
            vis[r][c] = True
            if matrix[r][c]:
                matrix[r][c] = val
                val+=1
            else:
                val = 1

            self.update_rec(matrix, vis, r+1, c, R, C, val)
            self.update_rec(matrix, vis, r-1, c, R, C, val)
            self.update_rec(matrix, vis, r, c+1, R, C, val)
            self.update_rec(matrix, vis, r, c-1, R, C, val)
    
    
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        vis = list()
        for i in range(len(matrix)):
            vis.append([False for _ in range(len(matrix[0]))])
        
        
        st =  deque()
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            for j in range(C):
                if not matrix[i][j]:
                   # self.update_rec(matrix, vis, i, j, len(matrix), len(matrix[0]), 0)
                   st.append((i, j, 0)) 
        while st:
            (r,c, val) = st.popleft()
            if r < 0 or c < 0 or r >= R or c >= C:
                continue
            
            if not vis[r][c] or (vis[r][c] and matrix[r][c] > val):
                matrix[r][c] = val
                vis[r][c] = True
                val+=1
                st.append((r+1, c, val))
                st.append((r-1, c, val))
                st.append((r, c+1, val))
                st.append((r, c-1, val))
        return matrix            