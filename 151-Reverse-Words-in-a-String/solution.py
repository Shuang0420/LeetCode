class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s=s.strip()
        words=re.split('\s+',s)
        return ' '.join(words[::-1])