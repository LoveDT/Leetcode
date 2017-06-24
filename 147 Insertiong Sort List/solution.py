# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head is None or head.next is None:
            return head
        alac = head.next
        prev = head
        while alac!=None:
            if prev.val<alac.val:
                prev = alac
                alac = alac.next
                if alac==None:
                    return head
            else:
                break
        start = head.next
        helper = head
        complete = ListNode(head.val)
        head.next = complete
        while start!=None:
            tmp = ListNode(start.val)
            start = start.next
            while complete!=None and tmp.val>=complete.val:
                helper = complete
                complete = complete.next
            helper.next = tmp
            tmp.next = complete
            helper = head
            complete = head.next
        return head.next