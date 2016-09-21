# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        root = TreeNode(nums[0])
        return self.helper(nums,root,0,len(nums)-1)
        
    def helper(self,nums,root, start,end):
        if start > end:
            return root
            
        if start == end:
            return TreeNode(nums[start])
        
        mid = start + (end - start)/2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums,root.left, start, mid-1)
        root.right = self.helper(nums,root.right, mid+1, end)
        
        return root