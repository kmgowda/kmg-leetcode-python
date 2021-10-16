// https://leetcode.com/problems/maximum-vacation-days

class Solution:
    def maxVacationDays1(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        NINF = float('-inf')
        N, K = len(days), len(days[0])
        best = [NINF] * N
        best[0] = 0
    
        for t in range(K):
            cur = [NINF] * N
            for i in range(N):
                for j, adj in enumerate(flights[i]):
                    if adj or i == j:
                        cur[j] = max(cur[j], best[i] + days[j][t])
            best = cur
        return max(best) 
    
    def maxVacationDays2(self, flights, days):
        if not flights: return None
        n=len(flights)
        k=len(days[0])
        if k==0: return 0
        dp=[[0]*n for j in range(k)] # representing the maximum days that you could play if given j weeks, ending in city i
        for i in range(0,n): flights[i][i]=1
        dp[0][0]=days[0][0]
        for i in range(1,n):
            if flights[0][i]==1:
                dp[0][i]=days[i][0]
            else:
                dp[0][i]=-1# it is impossible to endup in this city on day 0
        
        for j in range(1,k):
            for i in range(n):
                dp[j][i]=-1
                for q in range(n):
                     if dp[j-1][q]!=-1 and flights[q][i]==1:
                        dp[j][i]=max(days[i][j]+dp[j-1][q],dp[j][i])
 
        return max(dp[-1])


    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if not days:
            return 0

        n = len(days)
        k = len(days[0])
        dp = [[float('-inf') for i in range(n)] for week in range(k)]

        last = []
        for week in range(k):
            tmp = []
            for i in range(n):
                if week == 0:
                    if flights[0][i] or i == 0:
                        dp[0][i] = days[i][0]
                else:
                    for pair in last:
                        j = pair[1]
                        if flights[j][i] or j == i:
                            dp[week][i] = dp[week - 1][j] + days[i][week]
                            break
        
                tmp.append((dp[week][i], i))
            
            last = sorted(tmp, reverse=True)
        
        return last[0][0]