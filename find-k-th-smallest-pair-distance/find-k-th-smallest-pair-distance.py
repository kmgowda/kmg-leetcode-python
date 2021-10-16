// https://leetcode.com/problems/find-k-th-smallest-pair-distance

class Solution(object):

    
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l = None
        for i in range(1, len(nums)):
            diff = nums[i]-nums[i-1]
            if l == None or l > diff:
                  l = diff
        h = nums[-1]-nums[0]
        while l <= h:
            m = (l+h)>>1
            cnt = 0
            j = 0
            for i in range(len(nums)):
                while j < len(nums) and (nums[j]-nums[i])<=m:
                    j+=1
                cnt+=j-i-1
            if cnt >= k:
                h = m-1
            else:
                l = m+1

        return l        