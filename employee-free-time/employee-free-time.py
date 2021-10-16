// https://leetcode.com/problems/employee-free-time

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
from itertools import chain
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        work=sorted(chain(*schedule),key=lambda x: x.start)
        res=list()
        x=work[0]
        for y in work[1:]:
            if x.end < y.start:
                res.append(Interval(x.end,y.start))
                x=y
            elif y.end > x.end:
                x=y
        return res        