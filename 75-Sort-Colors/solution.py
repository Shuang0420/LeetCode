'''
Solution:
- quicksort?  Time complexity: O(nlogn)
- 3 numbers, so count and reset, Time complexity: O(n), Space complexity: O(3)->O(1), two-pass
- subarray with different states, Time complexity: O(n)

Attention:
- for solution 3, boundary is tricky, remember pointer is not included
'''
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return
        left,right,cur=0,len(nums)-1,0
        while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left]=nums[left],nums[cur]
                left+=1
                cur+=1
            elif nums[cur]==2:
                nums[cur],nums[right]=nums[right],nums[cur]
                right-=1
            else:
                cur+=1
            
        
        
    '''            
    # two-pass solution: count and reset            
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<1:
            return
        a0,a1,a2=0,0,0
        for n in nums:
            if n==0: a0+=1
            elif n==1: a1+=1
            elif n==2: a2+=1
        for i in range(len(nums)):
            if a0>0: 
                nums[i]=0
                a0-=1
            elif a1>0:
                nums[i]=1
                a1-=1
            elif a2>0:
                nums[i]=2
                a2-=1
    '''
            
                