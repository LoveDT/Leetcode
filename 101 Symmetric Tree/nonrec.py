# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        lvl,nxtlvl = [root],[]
        while len(lvl)!=0:
            l=0
            while l<(len(lvl)/2):
                if lvl[l]==None and lvl[-1-l]==None:
                    l+=1
                    continue
                if lvl[l]==None or lvl[-1-l]==None or lvl[l].val!=lvl[-1-l].val:
                    return False
                nxtlvl.append(lvl[l].left)
                nxtlvl.append(lvl[l].right)
                l+=1
            while l<len(lvl):
                if lvl[l]:
                    nxtlvl.append(lvl[l].left)
                    nxtlvl.append(lvl[l].right)
                    l+=1
            lvl=nxtlvl
            nxtlvl=[]
        return True