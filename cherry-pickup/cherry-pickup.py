// https://leetcode.com/problems/cherry-pickup

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[-1][-1]==-1: return 0
        memo={}

        # Enhance the grid
        N=len(grid)
        v,grid[-1][-1]=grid[-1][-1],-2
        grid.append([-1]*N)
        for row in grid: row.append(-1)

        def dp(i1,j1,i2,j2):
            if (i1,j1,i2,j2) not in memo:
                v1,v2=grid[i1][j1],grid[i2][j2]
                if v1==-1 or v2==-1: return -1
                if v1==v2==-2: return v
        
                s1=dp(i1+1,j1,i2+1,j2)
                s2=dp(i1+1,j1,i2,j2+1)
                s3=dp(i1,j1+1,i2+1,j2)
                s4=dp(i1,j1+1,i2,j2+1)
                res=max([s1,s2,s3,s4])
        
                if res!=-1: res+=grid[i1][j1]+(grid[i2][j2] if i1!=i2 or j1!=j2 else 0)
                memo[(i1,j1,i2,j2)]=res
            return memo[(i1,j1,i2,j2)]
        
        return max(dp(0,0,0,0),0)        