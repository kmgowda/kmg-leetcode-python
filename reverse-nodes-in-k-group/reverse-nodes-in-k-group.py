// https://leetcode.com/problems/reverse-nodes-in-k-group

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        def reverse(root):
            prv = None
            cur = root
            while cur:
                node = cur
                cur = cur.next
                node.next = prv
                prv = node
            return prv     
    
        def print_list(root):
            while root:
                print(root.val)
                root = root.next
                
        if not head or not head.next:
            return head
        cur = head
        tmp = head
        prv = tail = None
        newhead = head
        cnt = 0
        while cur:
            node = cur
            cur = cur.next
            node.next = prv
            prv = node
            cnt+=1
            if cnt == k:
                if tail:
                    tail.next = prv
                    tail = last
                else:
                    newhead = prv
                    tail =  head
                cnt = 0
                prv = None
                last = cur
  
        if prv:
            nexttail = reverse(prv)
        else:
            nexttail = None
        
        if tail:
            tail.next = nexttail
            return newhead
        else:
            return nexttail
        
                
                
            
            
        
                
                
                