# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        prevnode = None
        cur = head
        while cur is not None:
            nextnode = cur.next
            cur.next = prevnode
            prevnode = cur
            cur = nextnode
        return prevnode
        