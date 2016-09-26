class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums=sorted(nums)
        for i in range(1,len(nums),3):
            if nums[i]!=nums[i-1] or nums[i]!=nums[i+1]:
                return reduce(lambda x,y:x^y,nums[i-1:i+2])
        return nums[-1]