// https://leetcode.com/problems/permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        tmp = self.permute(nums[1:])
        ret = list()
        for lt in tmp:
            for i in range(len(lt)+1):
                ret.append(lt[:i]+[nums[0]]+lt[i:])
        return ret        
        