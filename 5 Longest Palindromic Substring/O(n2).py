class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or (len(s) == 0):
            return ""
        n = len(s)
        result = ""
        for i in range(n * 2 - 1):
            if i % 2 == 0:
                center = i / 2
                left, right = center, center
                while left > -1 and right < n and s[left] == s[right]:
                    if (right + 1 - left) > len(result):
                        result = s[left:right + 1]
                    left -= 1
                    right += 1
            else:
                left, right = i / 2, i / 2 + 1
                while left > -1 and right < n and s[left] == s[right]:
                    if (right + 1 - left) > len(result):
                        result = s[left:right + 1]
                    left -= 1
                    right += 1
            if len(result) > 2 * (n - i / 2):
                return result
        return result
        