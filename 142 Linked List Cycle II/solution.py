# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if not head:
            return None
        s,f = head,head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f is s:
                s = head
                while f is not s:
                    s = s.next
                    f = f.next
                return f
        return None
        