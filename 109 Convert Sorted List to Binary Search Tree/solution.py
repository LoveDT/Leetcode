# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        if head==None:
            return None
        if head.next==None:
            return TreeNode(head.val)
        l = ListNode(0)
        l.next,mid,r = head,l,head
        while r and r.next:
            r = r.next.next
            mid = mid.next
        r = mid.next
        mid.next = None
        root = TreeNode(r.val)
        root.left = self.sortedListToBST(l.next)
        root.right = self.sortedListToBST(r.next)
        return root
        