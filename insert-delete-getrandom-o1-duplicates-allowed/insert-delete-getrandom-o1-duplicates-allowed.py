// https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.d = collections.defaultdict(set)        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        b = val not in self.d
        self.d[val].add(len(self.l))
        self.l.append(val)
        return b
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        i, newVal = self.d[val].pop(), self.l[-1]
        if len(self.d[val]) == 0:
            del self.d[val]
        self.l[i] = newVal
        if newVal in self.d:
            self.d[newVal].add(i)
            self.d[newVal].discard(len(self.l)-1)
        self.l.pop()
        return True        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.l)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()