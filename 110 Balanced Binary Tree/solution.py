# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        return self.height(root)>=0
    def height(self,root):
        if root==None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return max(lh,rh)+1 if lh>=0 and rh>=0 and abs(lh-rh)<=1 else -1