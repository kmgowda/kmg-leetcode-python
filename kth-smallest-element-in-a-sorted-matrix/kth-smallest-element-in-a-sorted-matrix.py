// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution(object):
    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def merge(a, b):
            nums = list()
            i, j = 0,0
            while i < len(a) and j < len(b):
                 if a[i] < b[j]:
                        nums.append(a[i])
                        i+=1
                 else:
                       nums.append(b[j])
                       j+=1
            while i < len(a):
                nums.append(a[i])
                i+=1
            while j < len(b):
                nums.append(b[j])
                j+=1
            return nums    
        
        mer=list()
        for i in range(len(matrix)):
              mer= merge(mer, matrix[i])
 
        return mer[k-1] 

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        return sorted([y for x in matrix for y in x])[k-1]