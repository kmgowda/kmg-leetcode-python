// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        tmp = Node(insertVal, None)
        if not head:
            tmp.next = tmp
            return tmp
        prev = head
        cur = head.next
        while cur != head :
              if prev.val <= tmp.val and tmp.val <= cur.val:
                 break
              elif prev.val > cur.val:
                 if tmp.val >= prev.val or tmp.val <= cur.val:
                     break
              prev = cur
              cur = cur.next
        prev.next = tmp
        tmp.next = cur
        return head    