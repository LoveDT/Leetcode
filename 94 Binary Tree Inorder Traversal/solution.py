# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        if not root:
            return []
        result = []
        helper = []
        node = root
        while node:
            helper.append(node)
            node = node.left
        while helper:
            node = helper.pop()
            result.append(node.val)
            r = node.right
            while r:
                helper.append(r)
                r = r.left
        return result
        