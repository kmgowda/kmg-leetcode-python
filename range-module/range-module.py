// https://leetcode.com/problems/range-module

from bisect import bisect_left, bisect

class RangeModule(object):

    def __init__(self):
        self.range = [-float('inf'), float('inf')]

    def addRange(self, left, right):
        self._updateRange(left, right, 0)
        
    def queryRange(self, left, right):
        li = bisect(self.range, left)
        ri = bisect_left(self.range, right)
        return li == ri and li % 2 == 0
    
    def removeRange(self, left, right):
        self._updateRange(left, right, 1)

    def _updateRange(self, left, right, op):
        li = bisect_left(self.range, left)
        ri = bisect(self.range, right)
        
        if li % 2 == op:
            li = li - 1
            left = self.range[li]
        if ri % 2 == op:
            right = self.range[ri]
            ri += 1
            
        self.range[li:ri] = [left, right]
              


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)