# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node is None:
            return
        helper = node.next.val
        node.val = helper
        tmp = node.next
        node.next = node.next.next
        del tmp
        return 
        
        