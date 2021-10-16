// https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def reorder(cur, root):
            if not cur:
                return root
            node = reorder(cur.next, root)
            if not node:
                return node
            if node == cur or node.next == cur:
                cur.next = None
            else:    
                cur.next = node.next
                node.next = cur
            return cur.next
        
        reorder(head,head)     
            