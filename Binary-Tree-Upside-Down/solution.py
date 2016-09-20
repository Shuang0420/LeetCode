# Definition for a binary tree node.
'''
Three rules:

root's right node becomes the left node of the left node of root
root becomes the right node of root's left node
above rules apply on the left edge and return left node along the path.
'''


'''
newroot.right --> root.left.left
newroot --> root.left.right
newroot.left --> root.left.right
'''

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        stack = []
        # store the path
        while root:
            stack.append(root)
            root = root.left


        newRoot = stack.pop()
        head = newRoot
        while stack:
            parent = stack.pop()
            head.left = parent.right # parent
            head.right = parent

            head = parent
            parent.left = None
            parent.right = None

        return newRoot



class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # stop case
        if not root or not root.left:
            return root
        # assume all lower levels are handled
        newRoot = self.upsideDownBinaryTree(root.left)

        # handle current level
        root.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return newRoot
