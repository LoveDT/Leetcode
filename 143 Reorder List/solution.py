# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head == None:
            return
        if head.next == None:
            return
        if head.next.next == None:
            return
        l = ListNode(0)
        l.next,m,r = head,head,head
        l = l.next
        while r and r.next:
            r=r.next.next
            m = m.next
        r = m.next
        m.next = None
        r = self.reverseList(r)
        while l!=None and r!=None:
            m.next = r
            r = r.next
            m.next.next = l.next
            l.next = m.next
            l = m.next.next
            m.next = None
        return 
    def reverseList(self, head):
        if not head or not head.next:
            return head
        result = ListNode(0)
        result.next = head
        prev = head
        while prev.next:
            head = prev.next
            prev.next = head.next
            head.next = result.next
            result.next = head
        return result.next