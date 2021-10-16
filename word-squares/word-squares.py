// https://leetcode.com/problems/word-squares

class TrieNode:
    def __init__(self):
        self.words = None
        self.nxt = None

class Solution:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, root, word):
        cur = root
        for ch in word:
            if not cur.words:
                cur.words=list()
            cur.words.append(word)
            index = ord(ch)-ord('a')
            if not cur.nxt:
                cur.nxt = [None]*26
            if not cur.nxt[index]:
                cur.nxt[index]=TrieNode()
            cur = cur.nxt[index]
        if not cur.words:
            cur.words=list()

     
    def BuildTrie(self, words):
        for word in words:
            self.insert(self.root, word)
    
    def findSquares(self, ans, N, tmp):
        if len(tmp) == N:
            ans.append(tmp[:])
            return
         
        index = len(tmp)
        st =""
        for item in tmp:
            st +=item[index]

        cur = self.root
        for ch in st:
            index = ord(ch)-ord('a')
            if not cur.nxt or not cur.nxt[index]:
                cur = None
                break
            cur = cur.nxt[index]
        
        if not cur or not cur.words:
            return

        for word in cur.words:
            tmp.append(word)
            self.findSquares(ans, N, tmp)
            tmp.pop()
    
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        ans = list()
        if not len(words):
            return ans
        self.BuildTrie(words)
        self.findSquares(ans, len(words[0]), list())
        return ans
  
        