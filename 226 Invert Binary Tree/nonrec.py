# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return None
        resultseq = deque([])
        resultseq.append(root)
        while(len(resultseq)!=0):
            helper = resultseq[0]
            resultseq.popleft()
            tmp = helper.left
            helper.left = helper.right
            helper.right = tmp
            if helper.left:
                resultseq.append(helper.left)
            if helper.right:
                resultseq.append(helper.right)
        return root