// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        if not root:
            return root
        
        def print_tree_right(node):
            print("Print tree right")
            cur = node
            while cur:
                print("%d " %cur.val, end="")
                if node == cur.right:
                    break
                cur = cur.right
            print() 
 
        def print_tree_left(node):
            print("Print tree left")
            cur = node
            while cur:
                print("%d " %cur.val, end="")
                if node == cur.left:
                    break
                cur = cur.left
            print() 
            
        
        def dobulylist(node):
        
            if not node:
                return (None, None)
 
            lf, ll = dobulylist(node.left)
            rf, rl = dobulylist(node.right)
        
            if not lf:
                lf = node
                ll = node
                
            if not rl:
                rl = node
                rf = node

            rf.left = node
            ll.right = node                
            node.left = ll
            node.right = rf  

            lf.left = rl
            rl.right = lf
        
  
            #print_tree_right(lf)
            #print_tree_left(rl)
            return (lf, rl)
       
        (s, e) = dobulylist(root)
        return s
        

        
        
            
            