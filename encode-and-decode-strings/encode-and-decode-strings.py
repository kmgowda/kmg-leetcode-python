// https://leetcode.com/problems/encode-and-decode-strings

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        data=""
        header=str(len(strs)).zfill(4)
        for st in strs:
            header+=str(len(st)).zfill(4)
            data+=st
        header+=data
        return header
            

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        #print(s)
        out=[]
        N= int(s[:4])
        k = 4
        start=k+N*k
        #print(start)
        for i in range(N):
            l = int(s[k:k+4])
            out.append(s[start:start+l])
            start+=l
            k+=4
        return out    
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))