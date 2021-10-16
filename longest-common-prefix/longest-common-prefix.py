// https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minst= None
        minstid = None
        minstlen = None
        for i, name in enumerate(strs):
            l = len(name)
            if minstlen == None or minstlen > l:
                minstlen = l
                minstid = i
                minst = name
        prefix=""
        if not minst:
            return prefix
        for k, c in enumerate(minst):
            same = True
            for i, name in enumerate(strs):
                if i != minstid:
                    if c != name[k]:
                        same = False
                        break
            if same:
                prefix +=c
            else:
                break
        return prefix        
                
                
                    
        