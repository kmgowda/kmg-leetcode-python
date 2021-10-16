// https://leetcode.com/problems/unique-word-abbreviation

class ValidWordAbbr:

    def get_key(self, word):
        if len(word) < 3:
            return word
        st = str(len(word[1:-1]))
        return word[0]+st+word[-1]
    
    
    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.hashmap = {}
        for word in dictionary:
            key = self.get_key(word)
            if key not in self.hashmap:
                self.hashmap[key]= word
            elif self.hashmap[key]  != word:
                self.hashmap[key]=""
            
            
    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        key = self.get_key(word)
        if key not in self.hashmap:
            return True
        elif word == self.hashmap[key]:
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)