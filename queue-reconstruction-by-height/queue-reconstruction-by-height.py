// https://leetcode.com/problems/queue-reconstruction-by-height

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, k): (-h, k))
        q = []
        for p in people:
            q.insert(p[1], p)
        return q        