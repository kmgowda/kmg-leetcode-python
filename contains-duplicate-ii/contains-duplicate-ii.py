// https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map={}
        for i, n in enumerate(nums):
            if n not in map:
                map[n] = i
            elif (i - map[n]) <= k:
                return True
            elif (i-map[n]) > k:
                map[n] = i
        return False        
                
                    
        
            