// https://leetcode.com/problems/design-hit-counter

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=collections.deque()
 
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
  
        while (len(self.q) > 0) and  (timestamp - self.q[0] >= 300):
            self.q.popleft()
        self.q.append(timestamp)    

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
 
        while (len(self.q) > 0) and  (timestamp-self.q[0] >= 300):
             self.q.popleft()

        return len(self.q) 


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)