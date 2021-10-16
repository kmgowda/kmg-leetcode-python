// https://leetcode.com/problems/map-sum-pairs

class Node:
    def __init__(self):
        self.val = 0
        self.lt = None

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        tmp = self.root
        for c in key:
            index = ord(c)-ord('a')
            if not tmp.lt:
                tmp.lt = [None]*26
            if not tmp.lt[index]:
                tmp.lt[index] = Node()
            tmp = tmp.lt[index]
        if tmp != self.root:
            tmp.val = val

    
    def sum_rec(self, root):
        val = 0
        if root:
            val +=root.val
            if root.lt:
                for ch in root.lt:
                    val += self.sum_rec(ch)
        return val        
    
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        tmp = self.root
        i = 0
        N = len(prefix)
        while i < N:
            if not tmp.lt:
                return 0
            tmp = tmp.lt[ord(prefix[i])- ord('a')]
            if not tmp:
                return 0
            i+=1
        if tmp != self.root:
            return self.sum_rec(tmp)
        return 0
            
        
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)