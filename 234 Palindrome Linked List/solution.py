# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head==None or head.next==None:
            return True
        l = head
        prev = None
        while l.next!=None:
            l.prev = prev
            prev = l
            l = l.next
        tail = l
        tail.prev = prev
        while head.val == tail.val:
            if head==tail or (head.next==tail and head.val==tail.val):
                return True
            head = head.next
            tail = tail.prev
        return False
        
        