'''
Solution:
- subarray: 2 pointers: head,tail
- any repeated work? no   any meaningless work? yes    check the sum-array and we can find that the non-max-sum either subtract one more number or miss one more addition --> cur_sum=max(cur_sum,nums[start]+cur_sum)

'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum,max_sum=nums[0],nums[0]
        for start in range(1,len(nums)):
            cur_sum=max(nums[start],nums[start]+cur_sum)
            max_sum=max(cur_sum,max_sum)
        return max_sum
    '''
    # brute-force, time limit exceeded
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        global_sum=nums[0]
        for i in range(0,len(nums)-1):
            part_sum=nums[i]
            if part_sum>global_sum:
                global_sum=part_sum
            for j in range(i+1,len(nums)):
                part_sum+=nums[j]
                if part_sum>global_sum:
                    global_sum=part_sum
        part_sum=nums[-1]
        if part_sum>global_sum:
            global_sum=part_sum
        return global_sum
    '''
                