// https://leetcode.com/problems/alien-dictionary

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        less = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    less += a + b,
                    break
        chars = set(''.join(words))
        order = []
        while less:
            free = chars - set(zip(*less)[1])
            if not free:
                return ''
            order += free
            less = filter(free.isdisjoint, less)
            chars -= free
        return ''.join(order + list(chars))        