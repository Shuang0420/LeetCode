'''
recurse down
helper(node.left, global_max, node.val)
helper(node.right, global_max, node.val)

return up
max (curr_lengh, left_max_length, right_max_length)

current level
global_max = node.val == lastVal + 1 : length + 1 : 1
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        if not root:
            return 0

        return self.helper(root, 1, float('inf'))

    def helper(self, node, global_max, lastVal):
        if not node:
            return global_max
        global_max = global_max + 1 if node.val == lastVal + 1 else 1
        return max(global_max, self.helper(node.left, global_max, node.val), self.helper(node.right, global_max, node.val))
