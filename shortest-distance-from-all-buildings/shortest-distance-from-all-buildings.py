// https://leetcode.com/problems/shortest-distance-from-all-buildings

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        M = len(grid)
        if not M:
            return 0
        N = len(grid[0]) 
        dist = [[0]*N for _ in range(M)]
        hit =[[0]*N for _ in range(M)]
        
        def bfs(grid, i, j, ones):
            vis=[[False]*N for _ in range(M)]
     
    
            st= collections.deque() 
            st.append((i, j, 0))
                
            while st:
                (r,c, val)=st.popleft()
                #print("row= %d, col= %d, val=%d" %(r, c, val))

                for (k,l) in [(r+1, c), (r-1,c), (r,c+1), (r,c-1)]:
                    
                    if k >= 0 and l >=0 and k < M and l < N and not vis[k][l]:
                        vis[k][l] = True
                        
                        if grid[k][l] == 1:
                            ones-=1
                        elif not grid[k][l]:
                            hit[k][l] +=1
                            st.append((k,l,val+1))
                            dist[k][l]+=val+1
            
            return ones
        
        count=0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                        count+=1
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1 and bfs(grid, i, j, count):
                    return -1
                #elif grid[i][j] == 1:
                #    print(dist)
        
        #print(hit)
        #print("KMG")
        #print(dist)
                
        #print("KMG1")        
        return min([dist[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == count] or [-1])        
