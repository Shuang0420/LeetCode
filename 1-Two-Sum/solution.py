'''
Check assumption:
- array is not sorted
- each input would have exactly one solution
- duplicates in array

Solution:
1. Sort array, use start,end pointers to search target 9. Time complexity: O(nlogn)
2. Loop array, find if the remain of current number exists in the array(Don't loop current number). Time complexity: O(n^2)

Follow-up:
- Minimize time complexity: Use hashmap to store array index and value, so that the second loop for solution2 will have O(1) time complexity, and the total complexity would be O(n). The cost is space complexity.
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index1,value in enumerate(nums):
            for index2 in range(index1+1,len(nums)):
                if nums[index2]==target-value:
                    return [index1,index2]
        return None
        
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        

        return None
    '''