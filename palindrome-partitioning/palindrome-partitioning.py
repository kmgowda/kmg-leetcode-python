// https://leetcode.com/problems/palindrome-partitioning

class Solution(object):
    def partition1(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
            
        ans = [[] for _ in range(len(s)+1)]
        ans[0].append([])
        for i in range(len(s)):
            for start in range(i+1):
                if is_palindrome(s, start, i):
                    substr = s[start:i+1]
                    for parts in ans[start]:
                        ans[i+1].append(parts + [substr])
      
        return ans[-1]
    
    def partition(self, s):
        def dfs(s, path, res):
            if not s:
                res.append(path[:])
                return
            for i in range(1, len(s)+1):
                if s[:i] == s[i-1::-1]:
                    path.append(s[:i])
                    dfs(s[i:], path, res)
                    path.pop()        
        res = []
        dfs(s, [], res)
        return res    
    
                
        