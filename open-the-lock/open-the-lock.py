// https://leetcode.com/problems/open-the-lock

from collections import deque

class Solution(object):
   
    def openLock(self, deadends, target):
        def neighbors(node):
            ret = []
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    ret += [ node[:i] + str(y) + node[i+1:]]
            return ret        

        dead = set(deadends)
        queue = collections.deque([('0000', 0)])
        seen = {'0000'}
        while queue:
            node, depth = queue.popleft()
            if node == target: return depth
            if node in dead: continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth+1))
        return -1    
    
            