// https://leetcode.com/problems/remove-linked-list-elements

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        cur = head
        prev = None
        
        while cur:
            if cur.val == val:
                if prev:
                   prev.next = cur.next
                else:
                    head = cur.next
            else:        
                prev = cur
            cur = cur.next
        return head    
        