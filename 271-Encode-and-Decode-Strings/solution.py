class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return ''.join(['{:8}'.format(len(s))+s for s in strs])
        
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        index=0
        res=[]
        while index<len(s):
            length=int(s[index:index+8])
            index+=8
            res.append(s[index:index+length])
            index+=length
        return res
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))