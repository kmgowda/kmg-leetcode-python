// https://leetcode.com/problems/next-closest-time

class Solution(object):
    def nextClosestTime(self, T):
        Digit, time = list(set(T[:2] + T[3:])), list(T)
        for i, lim in ((4, '9'), (3, '5'), (1, ['9', '3'][time[0] == '2']), (0, '2')):
            try:    time[i] = min(d for d in Digit if time[i] < d <= lim); break
            except: time[i] = min(Digit)
        return ''.join(time)