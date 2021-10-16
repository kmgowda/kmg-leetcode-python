// https://leetcode.com/problems/design-linked-list

class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        
    def display(self, msg):
        print(msg)
        if self.head:
            print("head : %d" %self.head.val)
        if self.tail:
            print("tail : %d" %self.tail.val)
        cur = self.head
        while cur:
            print("%d" %cur.val)
            cur= cur.nxt
        print()    
        
        
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        
        cur = self.head
        i = 0
        while i < index and cur:
            cur = cur.nxt
            i+=1
#        self.display("get , fetching the value at index "+str(index))    
        if cur:
            print("found value %d" %cur.val)
            return cur.val
        else:
            return -1
        
            

            
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        tmp = Node(val)
        tmp.nxt = self.head
        self.head = tmp
        if not self.tail:
            self.tail = self.head
        
#        self.display("addAtHead , inserting "+str(val))
            
        
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        tmp = Node(val)
        if self.tail:
            self.tail.nxt = tmp
            k = self.tail
            self.tail = tmp
        else:
            self.head = tmp
            self.tail = tmp
            k = tmp
#        self.display("addAtTail , inserting "+str(val) +"after the value"+str(k.val))    
        
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index > 0 and not self.head:
            return
        
        tmp = Node(val)
        if index == 0 and not self.head:
            self.head = tmp
            self.tail = self.head
            return
        if index == 0 and self.head:
            tmp.nxt = self.head
            self.head = tmp 
            return
 
                 
        cur = self.head
        i = 1
        while i < index and cur:
            cur = cur.nxt
            i+=1
        if i == index:
            if not cur:
                if self.tail:
                    self.tail.nxt = tmp
                    self.tail = tmp
                else:
                    self.head = tmp
                    self.tail = tmp
#                print("KMG 1")
            else:
#                print("inserting after the value %d" %cur.val)
                tmp.nxt = cur.nxt
                cur.nxt = tmp
                if self.tail == cur:
                    self.tail = tmp
#                print("KMG 2")
#        else:
#            print("KMG 3")
#            print("i = %d" %i)
#        self.display("addAtIndex , inserting "+str(val)+" at index "+str(index)) 
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        cur = self.head
        prev = None
#        self.display("deleteAtIndex, deleting value at index "+str(index))
        if not index:
            head = head.nxt
            if self.tail == cur:
                self.tail = None
            del cur
            return
        
        i = 0
        while i < index and cur:
            prev = cur
            cur = cur.nxt
            i+=1
        if prev:
            if cur:
                prev.nxt = cur.nxt
                if self.tail == cur:
                    self.tail = prev
                del cur
#        self.display("deleteAtIndex, deleting value at index "+str(index) +"tail value "+str(self.tail.val)) 
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)