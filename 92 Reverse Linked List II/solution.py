# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if not head or not head.next or m==n:
            return head
        result = ListNode(0)
        result.next = head
        start = result
        for i in range(m-1):
            start = start.next
        l,r = start.next,start.next
        for i in range(n-m):
            l = r.next
            r.next = l.next
            l.next = start.next
            start.next = l
        return result.next if result!= start else start.next
        