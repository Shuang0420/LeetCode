class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        if n==2:
            return '11'
        result=self.helper([1,1],n-2)
        return ''.join([str(i) for i in result])
        
    def helper(self,list,n):
        if n==0:
            return list
        result=[]
        count,start,end=1,0,1
        while end<=len(list)-1:
            if list[start]==list[end]:
                count+=1
                end+=1
            else:
                result.append(count)
                result.append(list[start])
                start=end
                end+=1
                count=1
        if list[-1]==list[-2]:
            result.append(count)
            result.append(list[-1])
        else:
            result.append(count)
            result.append(list[-1])
        return self.helper(result,n-1)
            
