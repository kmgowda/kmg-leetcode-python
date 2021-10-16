// https://leetcode.com/problems/implement-stack-using-queues

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1= list()
        self.q2 = list()
        self.p = True
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.p:
            self.q1.append(x)
        else:
            self.q2.append(x)
            
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.p:
            while len(self.q1) > 1:
                self.q2.append(self.q1.pop(0))
            self.p = False
            return self.q1.pop(0)
        else:
            while len(self.q2) > 1:
                self.q1.append(self.q2.pop(0))
            self.p = True
            return self.q2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        top = 0
        if self.p:
            while len(self.q1):
                top = self.q1.pop(0)
                self.q2.append(top)
            self.p = False
        else:
            while len(self.q2):
                 top = self.q2.pop(0)
                 self.q1.append(top)
            self.p = True
        return top
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.p:
            if len(self.q1):
                return False
            else:
                return True
        else:
            if len(self.q2):
                return False
            else:
                return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()