// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, cur = None, None
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            tmp = ListNode(val%10)
            carry = val//10
            if not cur:
                head = tmp
            else:
                cur.next = tmp
            cur = tmp
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            val = l1.val + carry
            tmp = ListNode(val%10)
            carry = val//10
            if not cur:
                head = tmp
            else:
                cur.next = tmp
            cur = tmp
            l1 = l1.next

        while l2:
            val = l2.val + carry
            tmp = ListNode(val%10)
            carry = val//10
            if not cur:
                head = tmp
            else:
                cur.next = tmp
            cur = tmp
            l2 = l2.next
        
        if carry:
            cur.next = ListNode(carry)
        return head 
            
            
            
                
            
            
            