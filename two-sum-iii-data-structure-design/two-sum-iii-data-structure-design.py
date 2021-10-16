// https://leetcode.com/problems/two-sum-iii-data-structure-design

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map={}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.map:
            self.map[number]= False
        else:
            self.map[number]= True

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
       
        for key in self.map:
            if value-key == key and self.map[key] == True:
                 return True
            elif value-key != key and value-key in self.map:
                return True
        return False    

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)