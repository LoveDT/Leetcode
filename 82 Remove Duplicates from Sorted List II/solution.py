# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        prev = head
        cur = prev.next
        while prev.val==cur.val:
            del_val = prev.val
            while prev!=None and prev.val == del_val:
                prev = prev.next
            if prev is None:
                return None
            if prev.next is None:
                return prev
            head = prev
            cur = prev.next
        while cur and cur.next:
            if cur.val!=cur.next.val:
                prev = cur
                cur = cur.next
            else:
                del_val = cur.val
                while cur!=None and cur.val==del_val:
                    cur = cur.next
                prev.next = cur
        return head
        
                
        
        