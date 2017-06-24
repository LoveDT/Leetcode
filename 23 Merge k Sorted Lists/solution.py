"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        helper = []
        length = len(lists)
        if not length:
            return None
        for i in range(length):
            if lists[i]:
                helper.append((lists[i].val, lists[i]))
        heapq.heapify(helper)
        result = ListNode(0)
        cur = result
        while helper:
            tmp = heapq.heappop(helper)
            cur.next = ListNode(tmp[0])
            cur = cur.next
            if tmp[1].next:
                heapq.heappush(helper, (tmp[1].next.val, tmp[1].next))
        return result.next


