# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        s,f = ListNode(0),head
        s.next = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f is s:
                return True
        return False