# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root == None:
            return 0
        if root.left==None:
            return self.maxDepth(root.right)+1
        if root.right==None:
            return self.maxDepth(root.left)+1
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1