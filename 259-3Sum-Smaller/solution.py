class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return 0
        count=0
        nums=sorted(nums)
        for i in range(len(nums)):
            start=i+1
            end=len(nums)-1
            while start<end:
                cur_sum=nums[start]+nums[end]
                new_target=target-nums[i]
                if cur_sum<new_target:
                    count+=end-start
                    start+=1
                else:
                    end-=1
        return count