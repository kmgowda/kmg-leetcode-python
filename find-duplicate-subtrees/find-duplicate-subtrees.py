// https://leetcode.com/problems/find-duplicate-subtrees

class Solution:
    def __init__(self):
        self.map={}
    
    def findDuplicateSubtrees_rec(self, root):
        st=""
        if root:
            st+=self.findDuplicateSubtrees_rec(root.left)
            
            if st in self.map and self.map[st][0] > 1:
                lt = self.map[st][1]
            else:
                lt = list()
                
            if st != "" and st != str(root.val):
                st+=" "
            
            if st != str(root.val):
                 st+=str(root.val)
            
            if st != "" and st !=" ":
                 if st not in self.map:
                    self.map[st]=[1, [root]]
                 else:
                    self.map[st][0]+=1
                    for node in lt:
                        self.map[st][1].append(node)
            print(self.map) 
            st+=self.findDuplicateSubtrees_rec(root.right)
        return st    

 
    
    
    def findDuplicateSubtrees_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.findDuplicateSubtrees_rec(root)
        print(self.map)
        ret = list()
        for key in self.map:
            if self.map[key][0] > 1:
                tmp = list()
                for node in self.map[key][1]:
                    print("key = %s , val=%d " %(key,node.val))
                    if node.val not in tmp:
                         tmp.append(node.val)
                            
                ret.append(tmp)    
        return ret 

    def findDuplicateSubtrees(self, root):
        counts = {}
        ans = []
        def getId(root):
             if not root: return 0
             key = root.val << 32 | getId(root.left) << 16 | getId(root.right)
             if key not in counts:
                 counts[key] = [len(counts) + 1, 1]      
             else:
                 counts[key][1] += 1
             if counts[key][1] == 2: ans.append(root)
             return counts[key][0]    
        getId(root)
        return ans
    
    
    
    
    