// https://leetcode.com/problems/palindrome-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def rec_palindrome(self, slow, fast):
        if fast == None:
            # Even number of nodes
            return 1, slow
        elif fast.next == None:
            return -1, slow
        else:
            res, ptr = self.rec_palindrome(slow.next, fast.next.next)
            if res == -1:
                tmp = ptr.next
                if tmp.val != slow.val:
                    return 0, None
                else: 
                    return 1, tmp.next 
            elif res == 0:
                return 0, None
            elif res == 1:
                if ptr.val != slow.val:
                    return 0, None
                else:
                    return 1, ptr.next
            else:
                return res, None     
    
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        res, ptr = self.rec_palindrome(head, head)
        if res:
            return True
        else:
            return False
        