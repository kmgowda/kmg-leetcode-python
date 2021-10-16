// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        cur = head
        while cur:
            cur = cur.next
            l+=1
        
        if l < n:
            return cur
        elif l == n:
            cur = head.next
            del head
            return cur
        x = l-n-1
        cur = head
        for i in range(0, x):
            cur = cur.next
        
        tmp = cur.next
        if tmp:
            cur.next = tmp.next
            del tmp
        return head  
            
        
        