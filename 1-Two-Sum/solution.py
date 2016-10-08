'''
Check assumption:
- array is not sorted
- each input would have exactly one solution
- duplicates in array
- return index is not sorted

Corner case:
- len(nums)<2 or nums==None

Solution:
- Loop array, search target-nums[i] for each nums[j] on the right. Time complexity: O(n^2)

Attention:
- we cannot sort array, compare target and sum and move pointers to get the answer as it would disrupt the order
- array.index(value) returns first match, but this may not be what you expect

Optimization:
- While loop, use hashmap<target-nums[i],i> to store remaining index and value, so that the second loop will have O(1) time complexity, and the total complexity would be O(n). The cost is space complexity. This is two-pass solution.
- Two-pass --> One pass. While loop, for each i, check if it is in hashmap, if not, add it to the hashmap, if exists, return index.
'''

class Solution(object):
    
    # with hashmap
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums)<2:
            return None
        hashmap=dict()
        for index,value in enumerate(nums):
            if target-value in hashmap:
                return[index,hashmap[target-value]]
            hashmap[value]=index
        return None
    
    
    '''
    # two loops
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or len(nums)<2:
            return None
        for index1,value in enumerate(nums):
            for index2 in range(index1+1,len(nums)):
                if nums[index2]==target-value:
                    return [index1,index2]
        return None
    '''