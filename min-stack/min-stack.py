// https://leetcode.com/problems/min-stack

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.m = None
        self.st = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.m == None or x < self.m:
            self.m = x
        self.st.append(x)    
        

    def pop(self):
        """
        :rtype: void
        """
        x = self.st.pop()
        if self.m != None and x <= self.m:
            self.m = None
            for n in self.st:
                if self.m == None or self.m > n:
                    self.m = n
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.m
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()