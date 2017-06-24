# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        length = -1
        helper,result = ListNode(0),ListNode(0)
        lastnode = None
        helper.next = head
        result.next = head
        while helper:
            length+=1
            if helper.next==None:
                lastnode = helper
            helper = helper.next
        while k>=length:
            k=k%length
        helper = head
        while length-k>1:
            helper = helper.next
            length-=1
        lastnode.next = result.next
        result.next = helper.next
        helper.next = None
        return result.next