class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num or num == 0:
            return 0
        return (num - 1) % 9 + 1
        