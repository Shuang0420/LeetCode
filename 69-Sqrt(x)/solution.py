class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        '''
        Binary search, if use start<end-1, must consider start==end-1 at last 
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
        if end**2==x:
            return x
        return start  
                
            