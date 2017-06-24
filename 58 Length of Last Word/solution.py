class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if len(s)==0:
            return 0
        result = ""
        for i in range(len(s)):
            if s[-1-i]!=" ":
                result+=s[-1-i]
            elif len(result)!=0:
                break
        return len(result)
        