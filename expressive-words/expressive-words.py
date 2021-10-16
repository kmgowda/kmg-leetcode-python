// https://leetcode.com/problems/expressive-words

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def shrink(s):
            lt=list()
            prv = None
            cnt = 0
            for i, ch in enumerate(s):
                if not prv:
                    prv = ch
                    cnt = 1
                elif prv == ch:
                    cnt+=1
                else:
                    lt.append([prv, cnt])
                    prv = ch
                    cnt = 1
            lt.append([prv, cnt])        
            return lt        
        
        dst = shrink(S)
        ans = 0
        for word in words:
            ret = shrink(word)
            if len(ret) != len(dst): continue
            match = True
            for i, item in enumerate(ret):
                if item[0] != dst[i][0]:
                    match = False
                    break
                elif dst[i][1] > 2 and item[1] > dst[i][1]:
                    match = False
                    break
                elif dst[i][1] < 3 and dst[i][1] != item[1]:
                    match = False
                    break
            if match:
                ans+=1
        return ans        
                