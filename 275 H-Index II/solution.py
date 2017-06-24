class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations or len(citations) == 0:
            return 0
        n = len(citations)
        left, right = 0, n - 1
        if citations[-1] <= 0:
            return 0
        if citations[0] >= n:
            return n
        while left + 1 < right:
            mid = left + (right - left) / 2
            if (n - 1) - mid > citations[mid]:
                left = mid
            else:
                right = mid
        if (n - 1) - right < citations[right]:
            return n - right
        else:
            return n - right - 1
        