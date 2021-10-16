// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <= 0:
            return [[]]
        
        
        def permute_rec(arr):
            if len(arr) == 1:
                return [[arr[0]]]
            tmp = permute_rec(arr[1:])
            ret = list()
            for lt in tmp:
                for i in range(len(lt)+1):
                    nlt =  lt[:i]+[arr[0]]+lt[i:]
                    if nlt not in ret:
                        ret.append(nlt)
            return ret
        
        return permute_rec(nums)
