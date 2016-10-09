'''
Solution:
- convert to 2-sum problem, avoid duplicate triplets: sort the array, move pointers to skip duplicates

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            result+=self.twoSum(nums[i:],0-nums[i])
        return result
    
    
    def twoSum(self,nums,target):
        if len(nums)<3:
            return []
        start,end=1,len(nums)-1
        cur_res=[]
        while start<end:
            cur_sum=nums[start]+nums[end]
            if cur_sum<target:
                start+=1
            elif cur_sum>target:
                end-=1
            else:
                cur_res.append([nums[0],nums[start],nums[end]])
                start+=1
                end-=1
                while start<end and nums[start]==nums[start-1]:
                    start+=1
                while start<end and nums[end]==nums[end+1]:
                    end-=1
        return cur_res
        
        