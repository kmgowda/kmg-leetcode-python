// https://leetcode.com/problems/clone-graph

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def gen(self,node,map):
        if(node is None):
            return None
        clone = UndirectedGraphNode(node.label)
        map[clone.label]=clone
        for i in range(len(node.neighbors)):
            if(node.neighbors[i].label in map):
                clone.neighbors.append(map[node.neighbors[i].label])
            else:
                clone.neighbors.append(self.gen(node.neighbors[i],map))
        return clone    
    
    
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        map = {}
        return self.gen(node,map)
        