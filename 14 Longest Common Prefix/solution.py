class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or len(strs) == 0:
            return ""
        if len(strs[0]) == 0:
            return ""
        minlen = sys.maxint
        prefix = strs[0][0]
        for string in strs:
            minlen = min(minlen, len(string))
            if len(string) == 0 or string[0] != prefix:
                return ""
        for i in range(1, minlen):
            temp = strs[0][i]
            index = 1
            for j in range(1, len(strs)):
                index = j
                if strs[j][i] != temp:
                    index -= 1
                    break
            if index < len(strs) - 1:
                return prefix
            else:
                prefix += temp
        return prefix