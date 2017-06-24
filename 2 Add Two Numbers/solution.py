# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 if l1 else l2
        carry = 0
        result = ListNode(0)
        prev = result
        while l1 or l2:
            if l1 and l2:
                val = (l1.val + l2.val + carry)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = (l1.val + carry)
                l1 = l1.next
            else:
                val = (l2.val + carry)
                l2 = l2.next
            if (val) >= 10:
                carry = 1
            else:
                carry = 0
            cur = ListNode(val % 10)
            prev.next = cur
            prev = cur
        if carry == 1:
            last = ListNode(1)
            prev.next = last
        return result.next
        