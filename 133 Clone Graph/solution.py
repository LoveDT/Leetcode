# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneNode(self,node):
        if node==None:
            return None
        if node not in self.dic:
            self.dic[node] = UndirectedGraphNode(node.label)
            for item in node.neighbors:
                self.dic[node].neighbors.append(self.cloneNode(item))
        return self.dic[node]
    def cloneGraph(self, node):
        self.dic = {}
        return self.cloneNode(node)