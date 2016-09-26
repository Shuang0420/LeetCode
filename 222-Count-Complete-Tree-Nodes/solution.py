# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        '''
        Traversal would cause time limited exceed
        '''
        if not root:
            return 0
        left_height=self.left_height(root)
        right_height=self.right_height(root)
        # left subtree is full
        if left_height==right_height:
            return (1<<left_height)-1
        # right subtree is full
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
            
        
    def left_height(self,root):
        if not root:
            return 0
        return self.left_height(root.left)+1
        
        
    def right_height(self,root):
        if not root:
            return 0
        return self.right_height(root.right)+1
        