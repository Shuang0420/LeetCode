class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        nums=sorted(nums)
        for i in range(1,len(nums),3):
            if nums[i]!=nums[i-1] or nums[i]!=nums[i+1]:
                return reduce(lambda x,y:x^y,nums[i-1:i+2])
        return nums[-1]
        '''
        
        '''
        the code makes use of 2 variables. 
        ones - At any point of time, this variable holds XOR of all the elements which have 
        appeared "only" once. 
        twos - At any point of time, this variable holds XOR of all the elements which have 
        appeared "only" twice. 
        
        So if at any point time, 
        1. A new number appears - It gets XOR'd to the variable "ones". 
        2. A number gets repeated(appears twice) - It is removed from "ones" and XOR'd to the 
        variable "twice". 
        3. A number appears for the third time - It gets removed from both "ones" and "twice". 
        '''
        ones,twos=0,0
        for num in nums:
            twos |= num&ones
            ones ^= num
            not_three = ~(ones&twos)
            ones = ones&not_three
            twos = twos&not_three
        return ones
            
        
        
