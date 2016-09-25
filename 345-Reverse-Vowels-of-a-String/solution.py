class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        chars=[ord(i) for i in s]
        vowels=[ord(i) for i in ['a','e','i','o','u','A','E','I','O','U']]
        left,right=0,len(s)-1
        while left+1<=right:
            if chars[left] in vowels and chars[right] in vowels:
                if chars[left] != chars[right]:
                    chars[left],chars[right]=chars[right],chars[left]
                left+=1 
                right-=1
            if chars[left] not in vowels:
                left+=1
            if chars[right] not in vowels:
                right-=1
        return ''.join(chr(i) for i in chars)