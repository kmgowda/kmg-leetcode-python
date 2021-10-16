// https://leetcode.com/problems/basic-calculator

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_st(c):
            d={'+':2,'-':2,'(':0, "#":-1}
            return d.get(c,8)
        
        def get_exp(c):
            d={'+':1, '-':1,')':0, '(':9}
            return d.get(c, 7)
        
        
        def convert_postfix(s):
            tmp = re.split("(\+|\-|\(|\))", s.replace(" ",""))
            lt=filter(None, tmp)
            #print(lt)
            st=list()
            st.append("#")
            out=[]
            for c in lt:
                while get_st(st[-1]) > get_exp(c):
                    out.append(st.pop())
                
                if get_st(st[-1]) < get_exp(c):
                    st.append(c)
                else:
                    st.pop()
            while st[-1] !='#':
                out.append(st.pop())
            #print(out)    
            return out
        
        def evaluate(lt):
            st=[]
            for c in lt:
                if c == '+' or c =='-':
                    a = st.pop()
                    b = st.pop()
                    ans = a+b if c == '+' else b-a
                    st.append(ans)
                else:
                    st.append(int(c))
            return st[-1]        
            
  
        return evaluate(convert_postfix(s))
        
            
            