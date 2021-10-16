// https://leetcode.com/problems/merge-intervals

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def bisearch(vals, key):
            l = 0
            h = len(vals)-1
            while l <= h:
                m = (l+h)>>1
                if key < vals[m][0]:
                    h = m-1
                else:
                    l = m+1
            return l

        
        def insert(vals, intval):
            left = intval[0]
            right = intval[1]
            l = bisearch(vals, left)
            r = bisearch(vals, right)
            if l > 0 and vals[l-1][1] >= left:
                l-=1
                left=vals[l][0]
            if r > 0 and vals[r-1][1]> right:
                right = vals[r-1][1]
        
            vals[l:r]=[[left, right]]
        
        ret=[]
        #intervals.sort()
        for val in intervals:
            insert(ret, val)
        
        return ret      
