// https://leetcode.com/problems/find-peak-element

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        m = 0
        while l <= h:
            m = (l+h)//2
            if m > l  and m < h:
                if nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                    return m
                if nums[m] < nums[m+1]:
                    l = m+1
                else:
                    h = m-1
            elif l == m:
                if l+1 <= h:
                    if nums[m] > nums[m+1]:
                        return m
                    else:
                        return m+1
                else:
                    return m
            elif h == m:
                if h-1 >= l:
                    if nums[m] > nums[m-1]:
                        return m
                    else:
                        return m-1
                else:
                    return m
        return m    