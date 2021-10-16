// https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        slow = fast = head
        x = 0
        while x < k:
            fast = fast.next
            x+=1
            if not fast:
                fast = head
                k%=x
                x = 0
 
            
        while fast.next:
            fast = fast.next
            slow = slow.next
#        print("%d" %slow.val)    
        fast.next = head
        head = slow.next
        slow.next = None
        return head