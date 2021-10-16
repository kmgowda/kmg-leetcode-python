// https://leetcode.com/problems/3sum

from collections import Counter

class Solution:
    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = list()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if not nums[i]+nums[j]+nums[k] and [nums[i], nums[j], nums[k]] not in ret:
                        ret.append([nums[i], nums[j], nums[k]])
        return ret
    

    def threeSum(self, nums):
        nums.sort()
        d=Counter(nums)
        a, b =set(), set()
        for k in nums:
            d[k]-=1
            for i in a:
                if d[-(k+i)]>0 :
                    b.add((k,i,-(k+i)))
            a.add(k)
        return list(b)  