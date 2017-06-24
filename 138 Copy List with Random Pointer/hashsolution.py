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
        self.dict = {}
        return self.copyNode(head)
    def copyNode(self, node):
        if not node:
            return None
        if node not in self.dict:
            self.dict[node] = RandomListNode(node.label)
            if node.next and node.next not in self.dict:
                self.dict[node].next = self.copyNode(node.next)
            elif node.next:
                self.dict[node].next = self.dict[node.next]
            if node.random and node.random not in self.dict:
                self.dict[node].random = self.copyNode(node.random)
            elif node.random:
                self.dict[node].random = self.dict[node.random]
        return self.dict[node]
