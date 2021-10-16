// https://leetcode.com/problems/number-of-provinces


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        vis = [False]*N
  
        
        cnt=0  
        for i in range(N):
            if vis[i]:
                continue
            vis[i] = True    
            cnt+=1
            q = collections.deque()
            q.append(i)
            while q:
                k = q.popleft()
                for j in range(N):
                    if M[k][j] and not vis[j]:
                        vis[j] = True
                        q.append(j)
  
        return cnt            
  
                         
                        
                        
                    