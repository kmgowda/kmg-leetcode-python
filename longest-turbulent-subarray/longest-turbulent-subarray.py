// https://leetcode.com/problems/longest-turbulent-subarray

class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        one = 1
        mo = 1
        for i in range(len(A)-1):
            if i%2:
                if A[i] > A[i+1]:
                    one+=1
                else:
                    mo = max(mo, one)
                    one=1
            else:
                if A[i] < A[i+1]:
                    one+=1
                else:
                    mo = max(mo, one)
                    one=1
        mo = max(mo, one)            
        two = 1 
        mt = 1
        for i in range(len(A)-1):
            if i%2:
                if A[i] < A[i+1]:
                    two+=1
                else:
                    mt = max(mt, two)
                    two=1
            else:
                if A[i] > A[i+1]:
                     two+=1
                else:
                    mt = max(mt, two)
                    two=1
        mt = max(mt, two)            
        return max(mo,mt)            
                    
                    
                