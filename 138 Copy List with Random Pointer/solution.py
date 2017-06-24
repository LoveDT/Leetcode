# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return None
        # insert a new node after each node
        if not head.next:
            result = RandomListNode(head.label)
            result.next = head.next
            result.random = head.random
            return result
        cur = head
        while cur:
            tmp = RandomListNode(cur.label)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next
        # copy the random pointer
        rand = head
        while rand:
            if rand.random:
                rand.next.random = rand.random.next
            rand = rand.next.next
        # get the new list
        result = RandomListNode(0)
        result.next = head.next
        ret = head.next
        ori = head
        while ret.next:
            ori.next = ret.next
            ori = ori.next
            ret.next = ori.next
            ret = ret.next
        ori.next = None
        ret.next = None
        return result.next
