// https://leetcode.com/problems/design-circular-queue

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.k = k
        self.index = 0
        self.q = list()
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.index == self.k:
            return False
        else:
            self.q.append(value)
            self.index+=1
            return True
            

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.index == 0:
            return False
        else:
            self.q.pop(0)
            self.index-=1
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.index == 0:
            return -1
        else:
            return self.q[0]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.index == 0:
            return -1
        else:
            return self.q[self.index-1]      
        
  

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.index == 0:
            return True
        else:
            return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.index == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()