// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = list()
        for ch in tokens:
            if ch == '+':
                st.append(st.pop()+st.pop())
            elif ch == '-':
                f = st.pop()
                s = st.pop()
                st.append(s-f)
            elif ch == '*':
                st.append(st.pop()*st.pop())
            elif ch =='/':
                f = st.pop()
                s = st.pop()
                st.append(int(float(s)/float(f))) 
            else:
                st.append(int(ch))
 #           print("current char :"+ch)
 #           print(st)
 #           print
        return st[-1]   