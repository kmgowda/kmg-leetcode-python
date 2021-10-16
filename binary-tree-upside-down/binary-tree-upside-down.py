// https://leetcode.com/problems/binary-tree-upside-down

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        lt =[root]
        
        def traverse(node):
            if node:
                if node.right or node.left:
                    lt.append(node.right)
                    lt.append(node.left)
                traverse(node.right)
                traverse(node.left)
                
        
        traverse(root)
        st=[lt.pop()]
        head = st[-1]
  
        while len(st) > 0:
            node = st.pop()
            if node:
                if lt:
                    node.left = lt.pop()
                    st.append(node.left)
                else:
                    node.left = None
                if lt:
                    node.right = lt.pop()
                    st.append(node.right)
                else:
                    node.right = None
        return head    
                
                    