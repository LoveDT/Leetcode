class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num or len(num) == 0:
            return False
        n = len(num)
        for i in range(1, n/3 + 1): 
            for j in range(i + 1, 2 * n / 3 + 1):
                if num[i] == "0" and j - i > 1:
                    break
                a = int(num[:i])
                b = int(num[i:j])
                index = j
                while index != n:
                    c = a + b
                    if str(c) != num[index:index + len(str(c))] or index > n:
                        break
                    else:
                        a, b = b, c
                        index += len(str(c))
                        if index == n:
                            return True
        return False