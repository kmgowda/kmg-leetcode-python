// https://leetcode.com/problems/design-search-autocomplete-system

class Trie:
    def __init__(self):
        self.node = dict()
        self.words = list()


class AutocompleteSystem:
    def __init__(self, sentences, times):
        self.trie = Trie()
        self.cache_count = dict()
        self.keyword = ""
        for i, sen in enumerate(sentences):
            self._add_word(sen, self.trie)
            self.cache_count[sen] = times[i]

    def _add_word(self, word, trie):
        for char in word:
            if char not in trie.node:
                trie.node[char] = Trie()
            trie = trie.node[char]
            trie.words.append(word)
        return True

    def _find_words(self, word):
        trie = self.trie
        for char in word:
            if char in trie.node:
                trie = trie.node[char]
            else:
                return []
        return trie.words

    def input(self, c):
        if c != '#':
            self.keyword = self.keyword + c
            words = self._find_words(self.keyword)
            res = []
            for word in words:
                res.append((self.cache_count[word], word))
            res = list(set(res))
            return [s[1] for s in sorted(res, key=lambda x: (-x[0], x[1]))[:3]]
        else:
            self.cache_count[self.keyword] = self.cache_count.get(self.keyword,0) +1
            self._add_word(self.keyword,self.trie)            
            self.keyword = ""
        return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)