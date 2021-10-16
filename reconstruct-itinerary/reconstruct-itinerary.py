// https://leetcode.com/problems/reconstruct-itinerary

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            d[a] += [b]
       
        route = []
        
        def visit(airport):
            while d[airport]:
                visit(d[airport].pop())
            route.append(airport)
        
        visit('JFK')
        return route[::-1]
        
   
                
                    
                