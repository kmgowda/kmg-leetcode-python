// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size

class Solution(object):
    
    def binary_serach(self, reader, target, l, h):
  
        while l <= h:
             m = (l+h)//2
             if reader.get(m) == target:
                    return m
             if target > reader.get(m):
                l = m+1
             else:
                h = m-1
        return -1        
    
    
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        h = 1
        while reader.get(h) < target:
            h*=2
        return  self.binary_serach(reader, target, 0, h)   
            