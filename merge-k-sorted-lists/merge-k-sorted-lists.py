// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None
        cur = None
        cover = True
        while cover:
            cover = False
            minid = None
            for id, node in enumerate(lists):
                if node:
                    cover= True
                    if minid == None:
                        minid = id
                    elif lists[minid].val > node.val:
                        minid = id
            if minid != None:
                if not cur:
                    head = lists[minid]
                    cur = head
                else:
                    cur.next = lists[minid]
                    cur = cur.next
                lists[minid] = cur.next
                cur.next = None
            
        return head
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, cur = None, None
        
        while l1 and l2:
            if l1.val < l2.val:
                if not cur:
                    head = l1
                else:
                    cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                if not cur:
                    head = l2
                else:
                    cur.next = l2
                cur = l2
                l2 = l2.next

        if l1:
            if not cur:
                 head = l1
            else:
                 cur.next = l1

        if l2:
            if not cur:
                 head = l2
            else:
                 cur.next = l2

        return head    
    
    
    
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """    
        l = len(lists)
        while l > 1:
            index = 0
            for i in range(0, l, 2):
                if i+1 == l:
                    sec = None
                else:
                    sec = lists[i+1]
                lists[index]=self.mergeTwoLists(lists[i], sec)
                index+=1
            l  = (l+1)//2
        if lists:
            return lists[0]
        else:
            return None
            
            
    
            