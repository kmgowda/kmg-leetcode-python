// https://leetcode.com/problems/continuous-subarray-sum

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        for i in range(N):
            total = nums[i]
            for j in range(i+1, N):
                total+=nums[j]
                if (k != 0 and not total%k) or (k ==0 and not total):
                    return True
        return False        
        