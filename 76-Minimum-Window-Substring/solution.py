'''
two pointers representing substring in the middle, both pointers need to be decided to move or not in each iteration, decision based on whether the current character in T

store characters in T: -> search T: hashmap -> O(1)
when move start/end:
identify a match: counter
record the min length: global min

move end pointer
    -> find a match
move start pointer
    -> update global min
    -> remove a match
match count=0
hashmap<character,frequency>

followup:
hashmap -> arraymap, asscii, space complexity: O(126)
'''
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s or len(t)>len(s):
            return ''
        if len(t)==len(s) and t==s:
            return s
        hashmap=Counter(t)
        global_min,global_index,count=len(s),len(s),len(t)
        ls=list(s)
        start,end=0,0
        
        while end<len(s):
            if count>0:
                if ls[end] in hashmap:
                    hashmap[ls[end]]-=1
                    if hashmap[ls[end]]>=0:
                        count-=1
            end+=1
            while count==0:
                if global_min>=end-start:
                    global_index=start
                    global_min=end-start
                if ls[start] in hashmap:
                    if hashmap[ls[start]]>=0:
                        count+=1
                    hashmap[ls[start]]+=1
                start+=1
            
        return s[global_index:global_index+global_min]
                
                
                
        
        
        
        
        