// https://leetcode.com/problems/add-two-numbers-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def addTwnumber_rec(self, l1,l2):
        if not l1 and not l2:
           return None
        tmp = self.addTwnumber_rec(l1.next,l2.next)
        cur = ListNode(l1.val + l2.val)
        if tmp and tmp.val > 9:
            c = tmp.val//10
            tmp.val %=10
            cur.val +=c
            
        cur.next = tmp
        return cur    
        
    def addVal_rec(self, head, end, node):
        if head ==end :
           return node
        tmp = self.addVal_rec(head.next, end, node)
        cur = ListNode(head.val)
        if tmp.val > 9:
            c = tmp.val//10
            tmp.val %=10
            cur.val +=c
        cur.next = tmp
        return cur    
        
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        
        len1 = 0
        tmp = l1
        while tmp.next:
            len1 += 1
            tmp = tmp.next
        len2 = 0
        tmp = l2
        while tmp.next:
            len2 += 1
            tmp = tmp.next
        tmp1 = l1
        tmp2 = l2
    
        if len1 > len2:
            for i in range(len1-len2):
                  tmp1 = tmp1.next
        else:
            for i in range(len2-len1):
                  tmp2 = tmp2.next
        cur = self.addTwnumber_rec(tmp1, tmp2)
        head = None
        if len1 > len2:
            head = self.addVal_rec(l1, tmp1, cur)
        else:
            head = self.addVal_rec(l2, tmp2, cur)
        if head.val > 9:
            tmp = ListNode(head.val//10)
            head.val %=10
            tmp.next = head
            head = tmp
        return head    
            
        
                    
                    
        
        