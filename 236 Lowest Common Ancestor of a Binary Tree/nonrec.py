# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        pathp,pathq = self.findpath(root,p),self.findpath(root,q)
        length = min(len(pathp),len(pathq))
        result,x = None,0
        while x<length and pathp[x]==pathq[x]:
            result,x = pathp[x],x+1
        return result
    def findpath(self,root,target):
        path = []
        lastvisited = None
        while path or root:
            if root:
                path.append(root)
                root = root.left
            else:
                top = path[-1]
                if top.right and lastvisited!=top.right:
                    root = top.right
                else:
                    if top is target:
                        return path
                    lastvisited = path.pop()
                    root = None
        return path
        