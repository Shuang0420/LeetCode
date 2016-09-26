class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        '''
        for i in range(1,x/2):
            if (i-1)**2==x:
                return i-1
            elif (i-1)**2<x and i**2>x:
                return i-1
        '''
        start,end=0,x
        while start<end-1:
            mid=start+(end-start)/2
            if mid**2==x:
                return mid
            if mid**2>x:
                end=mid
            else:
                start=mid
        return start  
                
            