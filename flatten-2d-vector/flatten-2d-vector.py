// https://leetcode.com/problems/flatten-2d-vector

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.q=collections.deque()
        for t in vec2d:
            self.q.extend(t)

    def next(self):
        """
        :rtype: int
        """
        return self.q.popleft()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q)>0
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())