# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        if not root:
            return None
        helper = []
        node = root
        while node:
            helper.append(node)
            node = node.left
        count = 1
        while helper and count<=k:
            node = helper.pop()
            count+=1
            right = node.right
            while right:
                helper.append(right)
                right = right.left
        return node.val
        
        