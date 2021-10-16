// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        if not root:
            return None
        nq = list()
        bq = list()
        broot = TreeNode(root.val)
        nq.append(root)
        bq.append(broot)
        while any(nq):
            node = nq.pop(0)
            bnode = bq.pop(0)
            if any(node.children):
                rbnode = TreeNode(node.children[0].val)
                nq.append(node.children[0])
                bq.append(rbnode)
                bnode.right = rbnode
                cur = rbnode
                for i in range(1, len(node.children)):
                    nbnode = TreeNode(node.children[i].val)
                    cur.left = nbnode
                    nq.append(node.children[i])
                    bq.append(nbnode)
                    cur = nbnode
        return broot            
        

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        if not data:
            return None
        nq = list()
        bq = list()
        root = Node(data.val, list())
        nq.append(root)
        bq.append(data)
        while any(bq):
            bnode = bq.pop(0)
            node = nq.pop(0)
            if bnode.right:
                cur = bnode.right
                fnode = Node(cur.val, list())
                node.children.append(fnode)
                bq.append(cur)
                nq.append(fnode)
                while cur.left:
                    cur = cur.left
                    snode = Node(cur.val, list())
                    node.children.append(snode)
                    bq.append(cur)
                    nq.append(snode)
        return root                    
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))