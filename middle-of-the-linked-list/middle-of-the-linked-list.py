// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.mid = None
        def findMiddle(root, cur):
            if not cur:
                return root
            ret = findMiddle(root, cur.next)
            #print("ret.val = %d , cur.val=%d" %(ret.val, cur.val))
            if ret.next == cur or ret == cur:
                self.mid = cur
            return ret.next
               
        findMiddle(head, head)
        return self.mid
        