// https://leetcode.com/problems/flip-equivalent-binary-trees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def flip(root1, root2):
            res = False
            if root1 and root2:
                if root1.val != root2.val:
                    return False
                res = flip(root1.left, root2.left)
                if res:
                     res = flip(root1.right, root2.right)
                if not res:
                    res = flip(root1.left, root2.right) and flip(root1.right, root2.left)
                #print("root1 = %d, root2= %d, res = %d" %(root1.val, root2.val, res))                  
            else:
                if not root1 and not root2:
                    res = True
            return res
        
        return flip(root1, root2)
                