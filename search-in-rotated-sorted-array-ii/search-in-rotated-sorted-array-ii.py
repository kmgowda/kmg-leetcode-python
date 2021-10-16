// https://leetcode.com/problems/search-in-rotated-sorted-array-ii

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        else:
            l = 0
            h = len(nums)-1
            
            while (l <= h):
                m = (l+h)>>1
                
            
                if nums[m] == target:
                    return True
                
                while l < m and nums[l] == nums[m]: # tricky part
                    l += 1
                
                if nums[l] <= nums[m]:
                    if target >= nums[l] and target < nums[m]:
                        h = m-1
                    else:
                        l = m+1
                else:
                    if target > nums[m] and target <= nums[h]:
                        l = m+1
                    else:
                        h = m-1

            return False            