// https://leetcode.com/problems/encode-and-decode-tinyurl

import hashlib 
class Codec:
    
    def __init__(self):
        self.d={}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        hindx = hashlib.md5(longUrl)
        self.d[hindx] = longUrl
        return hindx
       
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.d[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))