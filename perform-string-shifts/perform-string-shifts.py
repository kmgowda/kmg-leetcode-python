// https://leetcode.com/problems/perform-string-shifts

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        dq = collections.deque(s)
        for d, p in shift:
            if d:
                for i in range(p):
                    dq.appendleft(dq.pop())
                   
            else:
                for i in range(p):
                    dq.append(dq.popleft())
        return ''.join(dq)            