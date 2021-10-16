// https://leetcode.com/problems/stream-of-characters

class StreamChecker:


    def __init__(self, words: List[str]):
        self.s = ''
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)
                

    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.dic[letter])
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)