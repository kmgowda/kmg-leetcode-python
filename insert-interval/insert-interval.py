// https://leetcode.com/problems/insert-interval

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e



class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def bisearch(vals, key):
            l = 0
            h = len(vals)-1
            while l <= h:
                m = (l+h) >>1
                if key < vals[m].start:
                    h = m-1
                else:
                    l = m+1
            return l    
        
        left = newInterval.start
        right = newInterval.end
        l = bisearch(intervals, left)
        r = bisearch(intervals, right)
        if l > 0 and intervals[l-1].end >= left:
            l-=1
            left = intervals[l].start
        if r > 0 and intervals[r-1].end > right:
            right = intervals[r-1].end
            
            
        intervals[l:r]=[Interval(left, right)]
        return intervals