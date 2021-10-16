// https://leetcode.com/problems/design-hashmap

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map={}

    def put(self, key, value):
        """
        value will always be positive.
        :type key: int
        :type value: int
        :rtype: void
        """
        self.map[key]=value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        ret = -1
        try:
            ret = self.map[key]
        except:
            pass
        return ret
        
        
    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        try:
            del self.map[key]
        except:
            pass


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)