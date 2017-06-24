# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = self.rec(root)
        return max(result)
    
    def rec(self, node):
        if not node:
            return (0, 0)
        else:
            left = self.rec(node.left)
            right = self.rec(node.right)
            return (node.val + left[1] + right[1], max(left) + max(right))