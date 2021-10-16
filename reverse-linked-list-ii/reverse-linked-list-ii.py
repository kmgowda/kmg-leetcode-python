// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        first, last, revh, revl, node = None, None, None, None, None
        cur = head
        i = 0
        while cur:
            i+=1
            node = cur
            cur = cur.next
            if i == m-1:
                first = node
            elif i == m:
                 revh, revl = node,node
            elif i > m and i <= n:
                node.next = revh
                revh = node
            elif i == n+1:
                last = node
                break
        
        if first:
            first.next = revh
        else:
            head = revh
        
        revl.next = last
        return head        
                
                
                