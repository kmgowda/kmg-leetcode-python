// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, cur = None, None
        
        while l1 and l2:
            if l1.val < l2.val:
                if not cur:
                    head = l1
                else:
                    cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                if not cur:
                    head = l2
                else:
                    cur.next = l2
                cur = l2
                l2 = l2.next

        if l1:
            if not cur:
                 head = l1
            else:
                 cur.next = l1

        if l2:
            if not cur:
                 head = l2
            else:
                 cur.next = l2

        return head    
            
            