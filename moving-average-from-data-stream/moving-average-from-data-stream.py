// https://leetcode.com/problems/moving-average-from-data-stream

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q = collections.deque()
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        if len(self.q) > self.size:
            self.q.popleft()
        return sum(self.q)/len(self.q)    


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)