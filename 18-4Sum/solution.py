class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums)<4:
            return []
        res=[]
        nums=sorted(nums)
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            res+=self.sum_3(nums[i:],target-nums[i])
        return res
        
    def sum_3(self,nums,target):
        if len(nums)<4:
            return []
        res=[]
        cur=nums[0]
        nums=nums[1:]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            new_target=target-nums[i]
            start=i+1
            end=len(nums)-1
            while start<end:
                cur_sum=nums[start]+nums[end]
                if cur_sum>new_target:
                    end-=1
                elif cur_sum<new_target:
                    start+=1
                else:
                    res.append([cur,nums[i],nums[start],nums[end]])
                    start+=1
                    end-=1
                    while start<end and nums[start]==nums[start-1]:
                        start+=1
                    while start<end and nums[end]==nums[end+1]:
                        end-=1
        return res
                