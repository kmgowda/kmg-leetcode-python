// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(l=n, r=n, st=""):
            if l < 0 or r < 0 or r < l:
                return
            else:
                if l == r == 0:
                    output.append(st)
                else:
                    backtrack(l-1, r, st+"(")
                    backtrack(l, r-1, st+")")
                
        output=list()
        backtrack()
        return output