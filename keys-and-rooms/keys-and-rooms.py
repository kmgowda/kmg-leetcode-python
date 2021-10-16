// https://leetcode.com/problems/keys-and-rooms

from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        vis =[False for _ in range(len(rooms))]
             
        st = deque()
        st.append(0)
        
        while st:
            r = st.popleft()
            vis[r] = True
            for k in rooms[r]:
                if not vis[k]:
                    st.append(k)
        for op in vis:
            if op == False:
                return False
        return True    
        