// https://leetcode.com/problems/lru-cache

class Node:
         def __init__(self, key, val):
            self.key = key
            self.val = val
            self.nxt = None
            self.prv = None
    

class HashDoublelinkedList:
         
         def __init__(self, capacity):
             self.max = capacity
             self.count = 0
             self.first = None
             self.last = None
             self.hash={}
            
         def display(self,msg):
             print(msg)
             print("***Begin***")
             print("hash values")   
             print(self.hash)
             cur = self.first
             print("from front") 
             while cur:
                   print("(%d, %d)" %(cur.key, cur.val))
                   cur = cur.nxt
             print("from tail")
             cur = self.last
             while cur:
                   print("(%d, %d)" %(cur.key, cur.val))
                   cur = cur.prv
             print("***End***")   
            
            
         def insert_front(self, key, val):
             tmp = Node(key, val)
             if not self.first:
                self.first = tmp
                self.last = self.first
             else:
                tmp.nxt = self.first
                self.first.prv = tmp
                self.first = tmp
             
             self.hash[key]=tmp
             self.count+=1 
             if self.count > self.max:
                 self.remove_last()
             #self.display("insert front")   
 
            
        
         def remove_last(self):
             if self.last:
                del self.hash[self.last.key]
                prv = self.last.prv
                self.last = prv
                if prv:
                    prv.nxt = None
                self.count-=1
              
 
            
         def find(self, key):
            if key in self.hash:
                node = self.hash[key]
                prv = node.prv
                if prv:
                    prv.nxt = node.nxt
                    if node.nxt:
                        node.nxt.prv = prv
                if node == self.last and node != self.first:
                    self.last = prv
                node.prv = None
                if node != self.first:
                    node.nxt = self.first
                    self.first.prv = node
                    self.first = node
                #self.display("find")    
                return node
            else:
                return None
            



class LRUCache(object):
  
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = HashDoublelinkedList(capacity)
 
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.find(key)
        if node:
            return node.val
        else:
            return -1
  
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.find(key)
        if node:
            node.val = value
        else:
            self.cache.insert_front(key, value)
            
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)