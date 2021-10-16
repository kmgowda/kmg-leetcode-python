// https://leetcode.com/problems/day-of-the-week

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3:
            month+=12
            year-=1
        y, c = year%100, year/100
        d = (13*(month+1)/5+y/4+c/4+y-2*c+day-1)%7
        return days[d]
            