class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        dictionary={'(':')','[':']','{':'}'}
        stack=[]
        for c in s:
            if c in dictionary.keys():
                stack.append(c)
            else:
                if not stack or c!=dictionary[stack.pop()]:
                    return False
        # return True if not stack else False
        return not stack
