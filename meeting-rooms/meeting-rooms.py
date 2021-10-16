// https://leetcode.com/problems/meeting-rooms

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        lt= sorted(intervals)
        for x, y in zip(lt, lt[1:]):
            if x[1] > y[0]:
                 return False
        return True    