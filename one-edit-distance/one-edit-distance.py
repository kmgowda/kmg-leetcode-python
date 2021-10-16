// https://leetcode.com/problems/one-edit-distance

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def onereplace(str1, str2, l):
            found = False
            for i in range(l):
                if str1[i] != str2[i]:
                    if found:
                        return False
                    else:
                        found = True 
            return found

        def oneinsert(str1, str2, l1, l2):
            id2 = 0
            id1 = 0
            while id1 < l1:
                if str1[id1] != str2[id2]:
                    if id1 != id2:
                        return False
                    else:
                        id2+=1
                else:
                    id1+=1
                    id2+=1
            if id1 == id2 and id2+1 == l2: return True
            elif id1+1 == id2 and id2 == l2: return True
            return False
        
        l1 = len(s)
        l2 = len(t)
        if (l1 == 0 and l2 == 1) or (l1 == 1 and l2 ==0): return True
        if abs(l1-l2) > 1: return False 
        if l1 == l2:
            return onereplace(s, t, l1)
        elif l1 < l2:
            return oneinsert(s, t, l1, l2)
        else:
            return oneinsert(t, s, l2, l1)
        
        