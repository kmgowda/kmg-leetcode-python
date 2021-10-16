// https://leetcode.com/problems/maximum-frequency-stack

class FreqStack(object):

    def __init__(self):
        self.d=collections.defaultdict(int)
        self.freq = collections.defaultdict(int)
        self.heap = []
        self.cnt = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.cnt+=1
        self.freq[x]+=1
        tmp = self.freq[x]<<32|self.cnt
        self.d[tmp]=x
        heapq.heappush(self.heap, -tmp)
        
        
        

    def pop(self):
        """
        :rtype: int
        """
        tmp = -heapq.heappop(self.heap)
        x = self.d[tmp]
        self.freq[x]-=1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()