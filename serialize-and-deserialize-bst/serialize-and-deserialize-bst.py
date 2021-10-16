// https://leetcode.com/problems/serialize-and-deserialize-bst

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        st = list()
        st.append(root)
        ret=""
        while any(st):
            node = st.pop()
            ret+=" "+str(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
 
        return ret        
            
    def insert_node(self, root, tmp):
        cur = root
        while cur:
            if tmp.val < cur.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = tmp
                    cur = None
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = tmp
                    cur = None
                    
                    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        if not len(data):
            return None
        root = None
        lt = data.split()
        for item in lt:
            tmp = TreeNode(int(item))
            if not root:
                root = tmp
            else:
                self.insert_node(root, tmp)
        return root        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))