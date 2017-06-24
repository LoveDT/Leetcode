# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxPathSum(self, root):
        result,helper = self.pathSum(root)
        return result
    def pathSum(self,root):
        if not root:
            return -sys.maxint, 0
        left = self.pathSum(root.left)
        right = self.pathSum(root.right)
        withroot = max(left[0],right[0],root.val+left[1]+right[1],root.val)
        woroot = max(left[1]+root.val,right[1]+root.val,0)
        return withroot, woroot
        