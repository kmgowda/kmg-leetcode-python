// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slow = head
        fast = head.next
        
        while fast and fast != slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        if not fast:
            return None
        
        l = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            l+=1
        fast = head
        while l > 0:
            fast = fast.next
            l-=1
        slow = head    
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow