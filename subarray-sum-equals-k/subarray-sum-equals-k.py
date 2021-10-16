// https://leetcode.com/problems/subarray-sum-equals-k

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = collections.defaultdict(int)
        sums[0]=1
        res = s = 0
        for n in nums:
            s += n 
            res += sums[s - k] 
            sums[s]+= 1            
        return res  
        