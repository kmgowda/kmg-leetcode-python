// https://leetcode.com/problems/design-hashset

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hash.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        try:
            self.hash.remove(key)
        except:
            pass
        

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hash:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)