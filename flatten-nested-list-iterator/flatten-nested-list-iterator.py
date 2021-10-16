// https://leetcode.com/problems/flatten-nested-list-iterator

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque

class NestedIterator(object):

    def flatten(self, nestedList):
        if nestedList == None:
            return None
        ret = deque()
        if isinstance(nestedList,list):
            for lt in nestedList:
                tmp = self.flatten(lt)
                ret.extend(tmp)
        elif nestedList.isInteger():
             ret.append(nestedList.getInteger())
        else:
            for lt in nestedList.getList():
                tmp = self.flatten(lt)
                ret.extend(tmp)
            
        return ret    
            

    
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.lt = self.flatten(nestedList)
                
        

    def next(self):
        """
        :rtype: int
        """
        return self.lt.popleft()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.lt) > 0
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())