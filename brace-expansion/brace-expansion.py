// https://leetcode.com/problems/brace-expansion

class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        lt , cur = list(), list()
        word=''
        for c in S:
            if c in [',', '{', '}']:
                if word:
                    cur.append(word)
                    word=''
                if c in ['{', '}'] and cur:
                    lt.append(sorted(cur))
                    cur = list()
            else:
                word+=c
        if word:
            cur.append(word)
        if cur:
            lt.append(cur)
                
        ret = list()
        for cur in lt:
            if not ret:
                ret = cur
                continue
            tmp = list()
            for line in ret:
                for word in cur:
                    tmp.append(line+word)
            ret = tmp        
           
        return ret    
                    