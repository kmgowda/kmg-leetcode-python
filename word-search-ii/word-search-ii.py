// https://leetcode.com/problems/word-search-ii

class TrieNode:
    def __init__(self):
        self.leaf = False
        self.nxt = None

class Solution:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, root, word):
        cur = root
        for c in word:
            index = ord(c)-ord('a')
            if not cur.nxt:
                cur.nxt = [None]*26
            if not cur.nxt[index]:
                cur.nxt[index] = TrieNode()
            cur = cur.nxt[index]    
        if cur != root:
            cur.leaf = True 
            
            
    def trie_search(self, board, i,j, root, visited, st, lt):
        if not root:
            return
        
        if root.leaf:
            if st not in lt:
                lt.append(st)
 
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[i]):
            return

        if visited[i][j] :
            return

        index = ord(board[i][j])-ord('a')
        if not root.nxt or not root.nxt[index]:
            return

        root = root.nxt[index]
        st +=board[i][j]
        visited[i][j]=True
        self.trie_search(board, i-1, j, root, visited, st, lt)
        self.trie_search(board, i+1, j, root, visited,st,lt)
        self.trie_search(board, i, j-1, root, visited,st, lt)
        self.trie_search(board, i, j+1, root, visited,st,lt)
 
        visited[i][j] = False

        return                   
    
    
    def dfs(self, board, i, j,  word, index, visited ):
        if index ==len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False
        if visited[i][j]:
            return False
        if board[i][j] != word[index]:
            return False
        visited[i][j]= True
        flag = (self.dfs(board, i-1, j, word, index+1, visited) or 
               self.dfs(board, i+1, j, word, index+1, visited) or
               self.dfs(board, i, j+1, word, index+1, visited) or
               self.dfs(board, i, j-1, word, index+1, visited))
        visited[i][j] = False
        return flag  
                    
    def search_singleword(self, board, word):
        visited = list()
        for k in range(len(board)):
            tmp = [False]*len(board[k])
            visited.append(tmp)        
        for i in range(len(board)):
            for j in range(len(board[i])):
                    if self.dfs(board, i, j, word, 0, visited):
                        return True
        return False       

    
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        lt = list()
        for word in words:
            self.insert(self.root, word)
        visited = list() 
        for k in range(len(board)):
            tmp = [False]*len(board[k])
            visited.append(tmp)    
            
        for i in range(len(board)):
            for j in range(len(board[i])):
                st=list()
                self.trie_search(board, i, j, self.root, visited, "", st)
                if any(st):
                    lt.extend(st)
  
        tmp = list()            
        for i in range(len(lt)-1, -1,-1):
            if lt[i] not in tmp:
                tmp.append(lt[i])
        return tmp     
 
 