// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow = head
        fast = head.next
        
        while fast and fast != slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        if not fast:
            return False
        return True
        
        