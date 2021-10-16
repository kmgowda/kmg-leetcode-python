// https://leetcode.com/problems/magical-string

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1, 2, 2]
        i = 2
        while len(nums) < n:
            nums.append(3 - nums[-1])
            if nums[i] == 2:
                nums.append(nums[-1])
            i += 1
        
        count = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
        return count       