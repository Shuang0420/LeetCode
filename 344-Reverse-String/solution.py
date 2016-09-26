class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        chars=list(s)
        start=0
        end=len(chars)-1
        while start<end:
            chars[start],chars[end]=chars[end],chars[start]
            start+=1
            end-=1
        return ''.join(chars)
            