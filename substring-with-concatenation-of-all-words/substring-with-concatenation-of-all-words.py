// https://leetcode.com/problems/substring-with-concatenation-of-all-words

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words: return []
        m, n, o, target = len(s), len(words), len(words[0]), []
        for i in range(m-n*o+1):
            word_target = words[:]
            for k in range(n):
                word = s[i+k*o:i+k*o+o]
                if word in word_target: word_target.remove(word)
                else: break
            if not word_target: target.append(i)
        return target  