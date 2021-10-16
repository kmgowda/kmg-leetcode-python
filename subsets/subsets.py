// https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = len(nums)
        N = pow(2,l)
        ret= list()
        for i in range(N):
            tmp = list()
            k = 0
            j = i
            
            for c in range(l):
                if j&1:
                    tmp.append(nums[k])
                j>>=1
                k+=1
            ret.append(tmp)    
        return ret 
                
        
        