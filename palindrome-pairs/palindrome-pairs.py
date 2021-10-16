// https://leetcode.com/problems/palindrome-pairs

class TrieNode:
      def __init__(self):
          self.isleaf = False
          self.nxt = None
          self.id = -1
          self.pos = None

class Solution:
    def __init__(self):
        self.root = TrieNode()
    

    def is_palindrome(self, word, f, l):
        while f < l:
            if word[f] != word[l]:
                return False
            f+=1
            l-=1
        return True    
    
    def palindromePairs1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ret = list()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                tmp = words[i]+words[j]
                if self.is_palindrome(tmp, 0, len(tmp)-1):
                    ret.append([i,j])
                tmp = words[j]+words[i]    
                if self.is_palindrome(tmp,0, len(tmp)-1):
                    ret.append([j,i])
        return ret 
    
    def insert(self, root, word, id):
        cur = root
        for i in range(len(word)-1, -1,-1):
            index = ord(word[i])-ord('a')
            if not cur.nxt:
                cur.nxt = [None]*26
            if not cur.nxt[index]:
                cur.nxt[index] = TrieNode()
            if self.is_palindrome(word, 0, i):
                if not cur.pos:
                    cur.pos = list()
                cur.pos.append(id)
            cur = cur.nxt[index]
        cur.id = id
        if not cur.pos:
              cur.pos = list()
        cur.pos.append(id)
        cur.isleaf = True
            
    
    def search(self, root, word, id, ret):
        cur = root
        for i, ch in enumerate(word):
            index = ord(ch)-ord('a')
            if cur.id > -1 and cur.id != id and self.is_palindrome(word , i, len(word)-1):
                ret.append([id, cur.id])
            if not cur.nxt or not cur.nxt[index]:
                return
            cur = cur.nxt[index]
        if not cur or not cur.pos:
            return
        for i in cur.pos:
            if i != id:
                ret.append([id, i])
        
            
    
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        for i, word in enumerate(words):
            self.insert(self.root, word, i)
        ret = list()    
        for i, word in enumerate(words):
             self.search(self.root, word, i,ret)
     #   print(ret)
        return ret
            
            
        
