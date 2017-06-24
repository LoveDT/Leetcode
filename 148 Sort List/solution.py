"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not head or not head.next:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        result = self.divide(head, length)
        return result
        
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        result = ListNode(0)
        cur = result
        while head1 and head2:
            if head1.val < head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next
        if not head1:
            cur.next = head2
            return result.next
        if not head2:
            cur.next = head1
            return result.next
    def divide(self, head, length):
        if length < 2:
            head.next = None
            return head
        n = length/2
        l, r = head, head
        for i in range(n):
            r = r.next
        h1 = self.divide(head, n)
        h2 = self.divide(r, length - n)
        return self.merge(h1, h2)
        
    
            
            
