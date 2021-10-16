// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):

    def flatten1(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        st = list()
        ret = None
        cur = None
        while head or any(st):
            if head:
                if not ret:
                    ret = head
                    head.prev = None
                else:
                    cur.next = head
                    head.prev = cur
                    cur.child = None
                cur = head
                if head.child:
                    if head.next:
                        st.append(head.next)
                    head = head.child
                else:
                    head = head.next
            elif any(st):
                head = st.pop()
        cur.child = None        
        return ret

    def flatten2(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        st = list()
        cur = head
        prev = None
        while cur or any(st):
            if cur:
                #print("%d" %cur.val)
                prev = cur
                if cur.child:
                    if cur.next:
                        st.append(cur.next)
                    cur = cur.child
                    prev.child = None
                    prev.next = cur
                    cur.prev = prev
                else:
                    cur = cur.next
            elif any(st):
                prev.next = st.pop()
                cur = prev.next
                cur.prev = prev
        return head

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = head
        while cur:
            if cur.child:
                ctail = cur.child
                while ctail.next:
                    ctail = ctail.next
                if cur.next:
                    cur.next.prev = ctail
                cur.child.prev = cur
                ctail.next = cur.next
                cur.next = cur.child
                cur.child = None

            cur = cur.next
            
        return head    
    
    
    
                