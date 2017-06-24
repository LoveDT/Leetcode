# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head==None:
            return head
        leng = 0
        r = head
        while r and leng<n:
            r = r.next
            leng+=1
        m = head
        while r:
            l = m
            m = m.next
            r = r.next
        if m==head:
            return head.next
        else:
            l.next = m.next
            del m
            return head
            
        