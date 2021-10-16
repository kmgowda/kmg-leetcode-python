// https://leetcode.com/problems/flood-fill

class Solution:
    
    def fill_rec(self, image, vis, r, c, R , C , col, newcol):
        if r > -1 and c > -1 and r < R and c < C and image[r][c] == col and not vis[r][c]:
            image[r][c] = newcol
            vis[r][c] = True
            self.fill_rec(image, vis, r+1, c, R, C, col, newcol)
            self.fill_rec(image, vis, r-1, c, R, C, col, newcol)
            self.fill_rec(image, vis, r, c+1, R, C, col, newcol)
            self.fill_rec(image, vis, r, c-1, R, C, col, newcol)
        
    
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        vis = list()
        for i in range(len(image)):
            vis.append([False for _ in range(len(image[0]))])
        
        self.fill_rec(image, vis, sr, sc, len(image), len(image[0]), image[sr][sc], newColor)
        return image
        