# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1==None or l2==None:
            return l1 if l1!=None else l2
        head1,head2 = l1,l2
        prev = None
        while head1!=None and head2!=None:
            if prev == None:
                prev = head1 if head1.val<head2.val else head2
                if prev is head1:
                    head1 = head1.next
                    if head1 == None:
                        prev.next = head2
                        break
                else:
                    head2 = head2.next
                    if head2 == None:
                        prev.next = head1
                        break
            if head1.val < head2.val:
                prev.next = head1
                prev = head1
                head1 = head1.next
            else:
                prev.next = head2
                prev = head2
                head2 = head2.next
        if head1==None:
            prev.next = head2
        else:
            prev.next = head1
        return l1 if l1.val<l2.val else l2
                
        