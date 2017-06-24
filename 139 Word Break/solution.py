class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        result = [False for i in range(len(s) + 1)]
        result[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if result[j] and s[j:i] in wordDict:
                    result[i] = True
                    break
        return result[-1]
        