// https://leetcode.com/problems/median-of-two-sorted-arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        l, h = 0, m
        while l <= h:
            px = (l+h)//2 
            py = (m+n+1)//2 - px
            maxx = nums1[px-1] if px > 0 else -float('inf')
            minx = nums1[px] if px < m else float('inf')
            maxy = nums2[py-1] if py > 0 else -float('inf')
            miny = nums2[py] if py < n else float('inf')
            
            if maxx <= miny and maxy<=minx:
                if (m+n)%2:
                    return max(maxx, maxy)
                else:
                    return (max(maxx, maxy)+min(minx,miny))/2.0
            elif maxx > miny:
                h = px-1
            else:
                l = px+1
        return float('inf')        