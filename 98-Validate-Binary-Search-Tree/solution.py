# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        list = self.getList(root)
        max = float('inf')
        while list:
            node = list.pop()
            if node >= max:
                return False
            max = node
        return True
        
    def getList(self, root):
        if not root:
            return []
        return self.getList(root.left)+[root.val]+self.getList(root.right)
        