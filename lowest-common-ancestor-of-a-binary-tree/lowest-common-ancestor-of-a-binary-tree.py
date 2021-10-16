// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def commonAncestor(root,n1,n2):
            if root == None:
                return None, False

            left, res = commonAncestor(root.left, n1, n2)
            if res:
                return left, True
            right, res = commonAncestor(root.right, n1, n2)
            if res:
                return right, True
            
            if left and right:
                if left == n1 and right == n2:
                    return root, True
                elif left == n2 and right == n1:
                    return root, True
 
            if root == n1:
                if left and left == n2:
                    return root, True
                elif right and right == n2:
                    return root, True
                else:
                    return root, False
            elif root == n2:
                if left and left == n1:
                    return root, True
                elif right and right == n1:
                    return root, True
                else:
                    return root, False
            else:
                if left and right:
                    return None, False
                elif left:
                    return left, False
                elif right:
                    return right, False
                else:
                    return None, False
        
                
        node, res = commonAncestor(root, p, q)
        if res:
            return node
        else:
            return None
        
        
                    
                