// https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        odd, even, ocur, ecur = None, None, None, None
        flag = True
        cur = head
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = None
            if flag:
                flag = False
                if not odd:
                    odd = tmp
                    ocur = tmp
                else:
                    ocur.next = tmp
                    ocur = tmp
            else:
                flag = True
                if not even:
                    even = tmp
                    ecur = tmp
                else:
                    ecur.next = tmp
                    ecur = tmp
        ocur.next = even
        return odd
        