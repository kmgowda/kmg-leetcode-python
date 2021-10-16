// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la = 0
        cur = headA
        while cur:
            cur = cur.next
            la+=1
        lb = 0
        cur = headB
        while cur:
            cur = cur.next
            lb+=1
        if lb > la:
            one = headB
            two = headA
            l = la
            h = lb
        else:
            one = headA
            two = headB
            l = lb
            h = la
            
        for i in range(l, h):
            one= one.next
        while one and two and one != two:
            one = one.next
            two = two.next
        return one    
        
            