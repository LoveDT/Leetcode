# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        helper = head.next
        prev = head
        result = ListNode(0)
        result.next = head
        fresult = ListNode(0)
        fresult.next = head.next
        while prev and helper:
            result.next = helper
            prev.next = helper.next
            helper.next = prev
            result = prev
            prev = prev.next
            if prev!= None:
                helper = prev.next
        return fresult.next
                
        