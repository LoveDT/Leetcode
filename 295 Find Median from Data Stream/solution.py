from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxheap = []
        self.minheap = []
        self.med = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxheap) == 0 and len(self.minheap) == 0:
            self.med = num
        if num <= self.med:
            heappush(self.maxheap, -num)
            if len(self.maxheap) > len(self.minheap) + 1:
                tmp = -1 * heappop(self.maxheap)
                heappush(self.minheap, tmp)
        elif num > self.med:
            heappush(self.minheap, num)
            if len(self.minheap) > len(self.maxheap) + 1:
                tmp = heappop(self.minheap)
                heappush(self.maxheap, -tmp)
        m, n = len(self.maxheap), len(self.minheap)
        if m == n:
            self.med = (self.minheap[0] - self.maxheap[0]) / 2.0
        elif m > n:
            self.med = -self.maxheap[0]
        else:
            self.med = self.minheap[0]

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return self.med
        

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()