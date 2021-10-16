// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        
        if len(nums) == 0:
            return 0
        
        max_len = 0
        running_sum = {0: -1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum not in running_sum:    
                running_sum[cur_sum] = i
            if (cur_sum - k) in running_sum:
                length = i - running_sum[cur_sum - k]
                max_len = max(max_len, length)                    
        return max_len
        
