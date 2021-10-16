// https://leetcode.com/problems/max-stack

class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.st.append(x)
 
        

    def pop(self):
        """
        :rtype: int
        """
        return self.st.pop()

        

    def top(self):
        """
        :rtype: int
        """
        return self.st[-1]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.st)

    def popMax(self):
        """
        :rtype: int
        """
        ma = max(self.st)
        ri = len(self.st)-self.st[::-1].index(ma)-1
        del self.st[ri]
        return ma
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()