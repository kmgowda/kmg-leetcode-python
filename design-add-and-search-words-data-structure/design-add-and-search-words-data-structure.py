// https://leetcode.com/problems/design-add-and-search-words-data-structure

class TrieNode:
    def __init__(self):
        self.isword = False
        self.next = None

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            index = ord(c)-ord('a')
            if not cur.next:
                cur.next = [None]*26
            if not cur.next[index]:
                cur.next[index]=TrieNode()
            cur = cur.next[index]
        if cur != self.root:
            cur.isword = True
            
    def search_rec(self, word, root):
        if not root:
            return False
        if not len(word):
            return root.isword
        flag = False
        if word[0] =='.':
            for i in range(26):
                if root.next and root.next[i]:
                    flag = self.search_rec(word[1:], root.next[i])
                if flag:
                    return True
        else:
            index = ord(word[0])-ord('a')
            if root.next and root.next[index]:
                return self.search_rec(word[1:], root.next[index])
        return flag
            

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.search_rec(word, self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)