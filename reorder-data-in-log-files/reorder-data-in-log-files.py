// https://leetcode.com/problems/reorder-data-in-log-files

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        d = collections.defaultdict(list)
        lt = list()
        for word in logs:
            k = word.find(' ')
            if word[k+1].isalpha():
                d[word[k+1:]]+=[word]
            else:
                lt+=[word]
        out=[]
        for k in sorted(d.keys()):
            for item in sorted(d[k]):
                out+=[item]
        for item in lt:
            out+=[item]
        return out    