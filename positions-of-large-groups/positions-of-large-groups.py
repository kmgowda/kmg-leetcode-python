// https://leetcode.com/problems/positions-of-large-groups

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        p = 0
        c = 0
        for i in range(1, len(S)):
            if S[p] == S[i]:
                c+=1
            else:
                if c-p > 1:
                    ret.append([p,c])
                p = i
                c = i
        if c-p > 1:
            ret.append([p,c])
            
        return ret        