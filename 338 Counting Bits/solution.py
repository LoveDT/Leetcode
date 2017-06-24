class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return []
        result = [0]
        pivot = 0
        for i in range(1, num + 1):
            if i == int(math.pow(2, pivot)):
                result.append(1)
                pivot += 1
            else:
                result.append(result[i - int(math.pow(2, pivot - 1))] + 1)
        return result
        