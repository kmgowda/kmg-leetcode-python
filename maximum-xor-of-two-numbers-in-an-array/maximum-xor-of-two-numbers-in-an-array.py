// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

class TrieNode:
    def __init__(self):
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def get_max(self, nums):
        m = None
        for item in nums:
            if not m:
                m = item
            else:
                if m < item:
                    m = item 
        return m
    
    def get_bits(self, num):
        for i in range(32):
            num >>=1
            if not num:
                return i+1
        return i    
    
    def insert(self, root, num, depth):
        for i in range(depth-1, -1, -1):
            if num&(1<<i):
                if not root.right:
                    root.right = TrieNode()
                root = root.right
            else:
                if not root.left:
                    root.left = TrieNode()
                root = root.left
 
    
    def get_max_xor_num(self, root, num,depth):
        ret = 0
        for i in range(depth-1, -1, -1):
            ret <<=1
            if num&(1<<i):
                if root.left:
                    root = root.left
                else:
                    root = root.right
                    ret |=1                
            else:
                if root.right:
                    root = root.right
                    ret |=1
                else:
                    root = root.left
        return ret    
            
        
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = self.get_max(nums)
        depth = self.get_bits(max_num)
#        print("depth = %d" %depth)
        #create the trie
        for item in nums:
            self.insert(self.root, item, depth)
            
        #get the max numbers 
        max_xor= None
        v1 = None
        v2 = None
        for item in nums:
            max_num = self.get_max_xor_num(self.root, item, depth)
            xor = max_num ^item
            if not max_xor:
                max_xor = xor
            if max_xor < xor:
                max_xor = xor
                v1 = item
                v2 = max_num
#        print("%d %d xor %d" %(v1, v2, max_xor))        
        return max_xor        


                      