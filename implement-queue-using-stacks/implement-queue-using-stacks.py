// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = list()
        self.s2 = list()
        self.p = True
        
        
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if not self.p:
            while len(self.s2):
                self.s1.append(self.s2.pop())
            self.p = True    
        self.s1.append(x)

        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.p:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            self.p = False
        return self.s2.pop()
  
        
        
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.p:
            return self.s1[0]
        else:
            return self.s2[-1]        
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if self.p:
            if len(self.s1):
                return False
            else:
                return True
        else:
            if len(self.s2):
                return False
            else:
                return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()