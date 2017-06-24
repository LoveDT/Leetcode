# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        result = ListNode(0)
        result.next = head
        helper = head
        while helper.next:
            if helper.val<helper.next.val:
                helper = helper.next
                continue
            prev = result
            while prev.next.val<helper.next.val:
                prev = prev.next
            tmp = helper.next
            helper.next = tmp.next
            tmp.next = prev.next
            prev.next = tmp
        return result.next
        