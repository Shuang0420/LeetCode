'''
Same with normal 3sum problem, just consider all possibilities.

Solution:
- sort nums, for nums[i] in nums, search if nums[start]+nums[end]<target-nums[i] for nums[i+1:], if it is, count+=end-start and keep going
'''
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