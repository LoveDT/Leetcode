class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
        if numRows >= len(s) or numRows == 1:
            return s
        up, down = 0, 1
        helper = [[] for i in range(numRows)]
        curRow = 0
        for i in range(len(s)):
            helper[curRow].append(s[i])
            if curRow == 0:
                up, down = 0, 1
                curRow += 1
            elif curRow == numRows - 1:
                up, down = 1, 0
                curRow -= 1
            else:
                if up:
                    curRow -= 1
                else:
                    curRow += 1
        return "".join("".join(c for c in element) for element in helper)
        