// https://leetcode.com/problems/number-of-islands

class Solution:
    def merge(self, grid, r, c, R, C):
        if r < 0 or c < 0  or  r >= R or c >= C or grid[r][c] != '1':
            return
        grid[r][c]='0'
        self.merge(grid, r+1, c, R, C)
        self.merge(grid, r, c+1, R , C)
        self.merge(grid, r-1, c, R , C)
        self.merge(grid, r, c-1, R, C)

        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        R = len(grid)
        if R == 0:
            return 0
        C = len(grid[0])
        count = 0
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count+=1
                    self.merge(grid, r, c, R, C)
                    
 
 
        return count