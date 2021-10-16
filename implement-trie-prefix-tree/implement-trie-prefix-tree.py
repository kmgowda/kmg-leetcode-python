// https://leetcode.com/problems/implement-trie-prefix-tree

class Node(object):
    def __init__(self):
        self.flag = False
        self.lt = None

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tmp1 = self.root
        for c in word:
            index = ord(c)-ord('a')
            if not tmp1.lt:
                tmp1.lt = [None]*26
            tmp = tmp1.lt[index]
            if not tmp:
                tmp1.lt[index] = Node()
            tmp1 = tmp1.lt[index]
        if tmp1 != self.root:        
            tmp1.flag = True        
                

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tmp = self.root
        i = 0
        N = len(word)
        while i < N:
            if not tmp.lt:
                return False
            tmp = tmp.lt[ord(word[i])- ord('a')]
            if not tmp:
                return False
            i+=1
        return tmp.flag
                
                   

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tmp = self.root
        i = 0
        N = len(prefix)
        while i < N:
            if not tmp.lt:
                return False
            tmp = tmp.lt[ord(prefix[i])- ord('a')]
            if not tmp:
                return False
            i+=1
        return True            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)