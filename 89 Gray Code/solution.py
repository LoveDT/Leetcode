class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        upper = 1 << n
        result = []
        for i in range(upper):
            cand = (i >> 1) ^ i
            result.append(cand)
        return result
        