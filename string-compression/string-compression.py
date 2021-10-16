// https://leetcode.com/problems/string-compression

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ar =collections.deque()
        i = 0
        prev=chars[0]
        for c in chars:
            if prev == c:
                i+=1
            else:
                ar.append((prev, i))
                prev=c
                i=1
        if i > 0:
             ar.append((prev, i))
        i=0
        while ar:
            (c, cnt)=ar.popleft()
            chars[i]=c
            i+=1
            if cnt > 1:
                for j in str(cnt):
                    chars[i]=str(j)
                    i+=1
        return i    
        
        