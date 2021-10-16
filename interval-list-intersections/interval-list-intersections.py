// https://leetcode.com/problems/interval-list-intersections

class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        M = len(A)
        N = len(B)
        i = j = 0
        ret = []
        
        def is_intersect(X, Y):
            if Y[0]<=X[0]<=Y[1] or  Y[0]<=X[1]<=Y[1]:
                return True
            if X[0]<=Y[0]<=X[1] and X[0]<=Y[1]<=X[1]:
                return True
            return False
        
        
        while i < M and j <N:
            if is_intersect(A[i], B[j]): 
                ret.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            if A[i][1] < B[j][1]:
               i+=1
            else:
               j+=1
        return ret    
                