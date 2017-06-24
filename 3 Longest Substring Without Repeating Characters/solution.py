class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        left, right, result = 0, 0, 0
        helper = {}
        while right < len(s):
            if s[right] in helper and left <= helper[s[right]]:
                left = helper[s[right]] + 1
            helper[s[right]] = right
            result = max(result, right - left + 1)
            right += 1
        return result