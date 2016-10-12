'''
Simliar to 3sum problem, but have a global_diff to record current minimum difference (remember it should be absolute value) and global_sum to record current closet result
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<3:
            return None
        nums=sorted(nums)
        global_diff=abs(target-nums[0])
        global_sum=sum(nums[0:3])
        for i in range(len(nums)-2):
            start=i+1
            end=len(nums)-1
            cur_target=target-nums[i]
            while start<end:
                sum2=nums[start]+nums[end]
                if sum2<cur_target:
                    if abs(cur_target-sum2)<global_diff: 
                        global_sum=sum2+nums[i]
                        global_diff=abs(cur_target-sum2)
                    start+=1
                elif sum2>cur_target:
                    if abs(sum2-cur_target)<global_diff: 
                        global_diff=abs(sum2-cur_target)
                        global_sum=sum2+nums[i]
                    end-=1
                else:
                    return target
        return global_sum
        