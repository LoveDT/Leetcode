# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if not head or not head.next:
            return head
        l,r = ListNode(0),ListNode(0)
        result,rstart = ListNode(0),ListNode(0)
        result.next = l
        rstart.next = r
        while head:
            if head.val<x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        l.next = rstart.next.next
        r.next = None
        return result.next.next
            
        