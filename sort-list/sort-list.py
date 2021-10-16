// https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(first, second):
            f = first
            s = second
            root = None
            while f and s:
                if f.val < s.val:
                    node = f
                    f = f.next
                else:
                    node = s
                    s = s.next
                if not root:
                    root = node
                    cur = node
                else:
                    cur.next= node
                    cur = node
            if not root:
                if f:
                    root = f
                else:
                    root = s
            else:       
                if f:
                    cur.next = f
                elif s:
                    cur.next = s
                else:
                    cur.next = None
                
            return root
        
        def find_middle(root):
            slow, fast = root, root
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def sort(root):
            if root is None or root.next is None:
                return root
            mid = find_middle(root)
            sroot = mid.next
            mid.next = None
            return merge(sort(root), sort(sroot))
        
        return sort(head)
            
    