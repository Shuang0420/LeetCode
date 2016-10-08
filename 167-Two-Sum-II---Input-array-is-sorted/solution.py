class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers or len(numbers)<2:
            return None
        start=0
        end=len(numbers)-1
        while start<end:
            sum=numbers[start]+numbers[end]
            if sum==target:
                return [start+1,end+1]
            if sum>target:
                end-=1
            else:
                start+=1
        return None
        