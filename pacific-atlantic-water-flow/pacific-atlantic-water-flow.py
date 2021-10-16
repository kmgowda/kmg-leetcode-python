// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution(object):
    def pacificAtlantic1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = list()
        M = len(matrix)
        if not M:
            return ret
        N = len(matrix[0])
        
        
        def bfs(r, c):
            vis=[[False]*N for _ in range(M)]
            q = collections.deque()
            q.append((r,c))
            vis[r][c] = True
            left, right = False, False
            while q:
                k, l = q.popleft()
                if k ==0 or l == 0:
                    left = True
                if k == M-1 or l == N-1:
                    right = True
                
                if left and right:
                    return True
                
                for (i, j) in [(k+1, l), (k-1,l), (k,l+1), (k, l-1)]:
                    if i < 0 or j < 0 or i >= M or j >= N:
                        continue
                    
                    if vis[i][j]:
                        continue
                        
                    vis[i][j] = True
                      
                    if matrix[i][j] <= matrix[k][l]:
                        q.append((i,j))
                        
            return False
        
        for i in range(M):
            for j in range(N):
                if bfs(i,j):
                    ret.append([i,j])
        return ret            

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(pq,pv):
            while pq:
                new_q = []
                for [x,y] in pq:
                    if pv[x][y]:
                        continue
                    pv[x][y] = True
                    if x > 0 and matrix[x-1][y] >= matrix[x][y]:
                        new_q.append([x-1,y])
                    if y > 0 and matrix[x][y-1] >= matrix[x][y]:
                        new_q.append([x,y-1])
                    if x+1 < m and matrix[x+1][y] >= matrix[x][y]:
                        new_q.append([x+1,y])
                    if y+1 < n and matrix[x][y+1] >= matrix[x][y]:
                        new_q.append([x,y+1])
                pq = new_q
            
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        ans = []
        pv, av = [[False for _ in range(n)] for _ in range(m)], [[False for _ in range(n)] for _ in range(m)]
        pq, aq = [[0,y] for y in range(1,n)] + [[x,0] for x in range(1,m)] + [[0,0]], [[m-1,y] for y in range(n-1)] + [[x,n-1] for x in range(m-1)]+[[m-1,n-1]]
        bfs(pq,pv)
        bfs(aq,av)
        for i in range(m):
            for j in range(n):
                if pv[i][j] == av[i][j] == True:
                    ans.append([i,j])
        return ans
    
    
    
    
    