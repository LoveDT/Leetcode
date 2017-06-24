# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        count = 0
        result = None
        p1,p2 = headA,headB
        while p1!=None and p2!=None:
            if p1 is p2:
                result = p1
                break
            p1 = p1.next
            p2 = p2.next
            if p1 is None and count==0:
                p1 = headB
                count+=1
            if p2 is None:
                p2 = headA
        return result