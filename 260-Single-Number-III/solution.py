class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = reduce(lambda x,y:x^y, nums)
        first_one_bit = left & ~(left-1)
        a,b=0,0
        for num in nums:
            if num&first_one_bit:
                a^=num
            else:
                b^=num
        return [a,b]