class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
            
        num,sign=0,1
        i=0 # start index
        maxint=(1<<31)-1
        str=str.strip()
        if str[0]=='+':
            i=1
        if str[0]=='-':
            sign=-1
            i=1
        
        for s in range(i,len(str)):
            if str[s] < '0' or str[s] > '9':
                break
            num=num*10+int(str[s])
            if num>maxint:
                break
            
        num*=sign
        if num>maxint:
            return maxint
        if num<-1*maxint:
            return -1*maxint-1
        return num
            
        