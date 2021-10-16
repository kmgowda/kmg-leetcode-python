// https://leetcode.com/problems/word-break

import functools
class Trie:
    def __init__(self):
        self.nxt = collections.defaultdict(Trie)
        self.isword = False

        
class Solution(object):
    def __init__(self):
        self.root = Trie()
        
    def insert(self, word):
        cur = self.root
        
        for ch in word:
            if not cur.nxt[ch]:
                cur.nxt[ch]=Trie()
            cur = cur.nxt[ch]
        cur.isword = True    

    def memoize(func):
        cache = dict()

        def memoized_func(*args):
            if args in cache:
                return cache[args]
            result = func(*args)
            cache[args] = result
            return result

        return memoized_func
        
    @functools.lru_cache(maxsize=128)
    def search(self, word, i, N, root, cur):
        if not cur:
            return False
        
        i+=1
        if i == N:
            return True if cur.isword else False

        ret = self.search(word, i, N, root, cur.nxt[word[i]])
  
        if not ret and cur.isword:
            ret =  self.search(word, i, N, root, root.nxt[word[i]])
        
        return ret
  


    @functools.lru_cache(maxsize=128)
    def search_it(self, word, i, N, root, cur):
        q=collections.deque()
        q.append((cur, i))
        while q:
            cur, i = q.pop()
            if not cur:
                continue
            i+=1
            if i == N:
                if cur.isword:
                    return True
                else:
                    continue
            
            if cur.isword:
                q.append((root.nxt[word[i]], i))
            q.append((cur.nxt[word[i]], i))
  
        return False    
        
    
    
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        for word in wordDict:
            self.insert(word)
        return self.search(s, -1, len(s), self.root, self.root)
    
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1,n+1):
            for w in wordDict:
                #print(s[i-len(w):i])
                if dp[i-len(w)] and s[i-len(w):i]==w:
                    dp[i]=True
        return dp[-1] 

    