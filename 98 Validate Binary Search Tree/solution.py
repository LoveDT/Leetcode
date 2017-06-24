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
        result = self.validBST(root, -sys.maxint, sys.maxint)
        return result
    
    def validBST(self, node, lower, upper):
        if not node:
            return True
        if node.val <= lower or node.val >= upper:
            return False
        else:
            return self.validBST(node.left, lower, node.val) and self.validBST(node.right, node.val, upper)