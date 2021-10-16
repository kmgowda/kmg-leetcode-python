// https://leetcode.com/problems/zigzag-iterator

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        if len(self.v1) > 0:
            self.one = True
        elif len(self.v2) > 0:
            self.one = False
        else:
            self.one = None

    def next(self):
        """
        :rtype: int
        """
        if self.one == None:
            return -1
        
        if self.one:
             val = self.v1.pop(0)
             if len(self.v2) > 0:
                self.one = False
        else:
             val = self.v2.pop(0)
             if len(self.v1) > 0:
                self.one = True
        return val        
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return (len(self.v1) > 0) or (len(self.v2) > 0)
    

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())