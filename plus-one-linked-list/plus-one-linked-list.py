// https://leetcode.com/problems/plus-one-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def addone(root):
            if not root:
                return 1
            r = addone(root.next)
            root.val+=r
            r = root.val//10
            root.val%=10
            return r
        
        if not head:
            return head
        
        ret = addone(head)
        
        if ret > 0:
            root = ListNode(ret)
            root.next= head
        else:
            root = head
        return root    