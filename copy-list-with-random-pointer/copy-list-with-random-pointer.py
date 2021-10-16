// https://leetcode.com/problems/copy-list-with-random-pointer

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    
    def display(self, head, msg):
        print(msg)
        while head:
            print(str(head.label))
            head = head.next
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        self.display(head, "original linked list")   
        cur = head
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.random = cur
            cur = cur.next
            tmp.random.next = tmp
            tmp.next = cur
        self.display(head, "Modified linked list")   
        cur = head.next
        while cur:
              if cur.random.random:
                  cur.random = cur.random.random.next
              else:
                  cur.random = None
              cur = cur.next
              if cur:
                  cur = cur.next
 
        clone = None
        cur = head
        clcur = None
        prev = None
        while cur:
             if prev:
                  prev.next = cur
             prev = cur  
             cur = cur.next
             if cur:
                if clcur:
                     clcur.next = cur
                else:
                     clone = cur
                clcur = cur
                cur = cur.next
        prev.next = None        
           
        return clone    
                
            