# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
recursive down: 
  pass the array, and two pointers (start, end) down
  for the left child, use mid-1 as end
  for the right child, use mid+1 as start
return up: 
  return the root of subtree
current level: 
  build the subtree
  mid=left+(right-left)/2
  root=TreeNode(nums[mid])
  root.left=helper(nums,start,mid-1)
  root.right=helper(nums,mid+1,end)
base case:
  if start>end:
    return None
  if start==end:
    return TreeNode(start)
'''
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.helper(nums,0,len(nums)-1)
        
    def helper(self, nums, start, end):
        if start>end:
            return None
        if start==end:
            return TreeNode(nums[start])
        mid=start+(end-start)/2
        root=TreeNode(nums[mid])
        root.left=self.helper(nums,start,mid-1)
        root.right=self.helper(nums,mid+1,end)
        return root
       

