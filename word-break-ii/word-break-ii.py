// https://leetcode.com/problems/word-break-ii

class Solution(object):
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
        
        if dp[-1] == False:
            return []
        
        pos = []
        
        for i in range(1, len(dp)):
            if dp[i] == True:
                pos.append(i)
   
        res = []
        self.build(pos, s, "", res,  0, len(pos))
        return res
    
    def build(self, pos, s, path, res, start, N):
        if start >= N:
            res.append(path[:])
            return 
        
        for i in range(start, N):
              self.build(pos, s, path+s[start:pos[i]]+" ", res, i, N)
                
                
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
    
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for item in rest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res                