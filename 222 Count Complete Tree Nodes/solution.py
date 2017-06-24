# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result, height, marker, fulllevel = 0, 0, root, 1
        while marker:
            result += fulllevel
            fulllevel *= 2
            height += 1
            marker = marker.right
        lvl, flag = 1, 0
        realheight = self.findheight(root)
        if realheight == height:
            return result
        while lvl < realheight:
            leftheight, rightheight = self.findheight(root.left), self.findheight(root.right)
            if leftheight == rightheight:
                root = root.right
                if lvl == realheight - 1:
                    result += 2
                else:
                    result += int(math.pow(2, realheight - lvl - 1))
                flag = 0
            else:
                root = root.left
                flag = 1
            lvl += 1
        return result + flag
        
    def findheight(self, root):
        if not root:
            return 0
        else:
            return 1 + self.findheight(root.left)
        