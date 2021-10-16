// https://leetcode.com/problems/add-binary

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a)-1
        j = len(b)-1
        ret =""
        carry = False
    
        while i >=0 and j >=0:
            if carry:
                if a[i]=='1' and b[j]=='1':
                    ret ="1"+ret
                elif a[i]=='1' and b[j]=='0':
                    ret ="0"+ret
                elif a[i]=='0' and b[j]=='1':
                    ret = "0"+ret
                else:
                    ret="1"+ret
                    carry = False
            else:
                if a[i]=='1' and b[j]=='1':
                    ret ="0"+ret
                    carry = True
                elif a[i]=='1' and b[j]=='0':
                    ret ="1"+ret
                elif a[i]=='0' and b[j]=='1':
                    ret ="1"+ret
                else:
                    print("KMG")
                    ret="0"+ret
            i-=1
            j-=1
            
        while i >=0:
            if carry:
                if a[i]=='1':
                    ret="0"+ret
                else:
                    ret="1"+ret
                    carry = False
            else:
                if a[i]=='1':
                    ret="1"+ret
                else:
                    ret="0"+ret
            i-=1        
        while j >=0:
            if carry:
                if b[j]=='1':
                    ret="0"+ret
                else:
                    ret="1"+ret
                    carry = False
            else:
                if b[j]=='1':
                    ret="1"+ret
                else:
                    ret="0"+ret
            j-=1
            
        if carry:
            ret = "1"+ret

        return ret     