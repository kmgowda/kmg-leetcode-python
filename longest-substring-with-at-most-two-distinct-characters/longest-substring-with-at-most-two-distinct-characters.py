// https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = list()
        ans = cnt = 0
        prev=''
        pcnt=0
        for i, ch in enumerate(s):
            size = len(st)
            if size == 0:
                st.append(ch)
                cnt+=1
            elif size == 1:
                if st[-1] !=  ch:
                      st.append(ch)
                cnt+=1        
            else:
                if ch in st:
                    cnt+=1
                else:
                    ans = max(ans, cnt)
                    del st[:]
                    st.append(prev)
                    st.append(s[i])
                    cnt= pcnt+1
            if prev == ch:
                pcnt+=1
            else:
                prev = ch
                pcnt = 1
            
            
        return max(ans, cnt)                     
        
                
                