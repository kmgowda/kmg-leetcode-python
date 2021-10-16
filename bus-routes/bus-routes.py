// https://leetcode.com/problems/bus-routes

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        st, travel, bcount, vis = collections.defaultdict(set), [S], 0,  collections.defaultdict(bool)
        for i, route in enumerate(routes):
            for bus in route:
                st[bus].add(i)
                
        while travel:
            new = []
            for stop in travel:
                if stop == T:
                    return bcount
                for b in st[stop]:
                    if not vis[b]:
                        vis[b] = True
                        for nextstop in routes[b]:
                            if nextstop != stop:
                                new.append(nextstop)
            bcount += 1
            travel = new
        return -1