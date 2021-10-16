// https://leetcode.com/problems/4sum-ii

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N = len(A)
        map1={}
        map2={}
        for i in range(N):
            for j in range(N):
                s = A[i]+B[j]
                if s not in map1:
                    map1[s]= 1
                else:
                    map1[s]+=1
                s = C[i]+D[j]
                if s not in map2:
                    map2[s]= 1
                else:
                    map2[s]+=1
        count = 0
        for k1 in map1:
            k2 = -1*k1
            if k2 in map2:
                count+=(map1[k1]*map2[k2])
        return count                    
                    
            