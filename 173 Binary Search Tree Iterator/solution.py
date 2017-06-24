# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.result = []
        while root:
            self.result.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.result

    # @return an integer, the next smallest number
    def next(self):
        tmp = self.result.pop()
        start = tmp.right
        while start:
            self.result.append(start)
            start = start.left
        return tmp.val
        
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())