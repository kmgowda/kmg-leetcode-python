// https://leetcode.com/problems/combination-sum-iv

class Solution(object):
    def __init__(self):
        self.dp = {}
        
    def combinationSum4(self, nums, target):
        nums.sort()
        def dfs(val):
            if val == 0:
                return 1
            elif val < 0:
                return -1           
            
            if val in self.dp:
                return self.dp[val]
            
            ans = 0  
            for num in nums:
                ret = dfs(val-num)
                if ret == -1: 
                    break
                else:
                    ans += ret
            self.dp[val] = ans
            return ans
        
        return dfs(target)