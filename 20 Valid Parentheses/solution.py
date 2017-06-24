class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) % 2 == 1:
            return False
        n = len(s)
        helper = []
        for i in range(n):
            if s[i] == "(":
                helper.append(")")
            elif s[i] == "[":
                helper.append("]")
            elif s[i] == "{":
                helper.append("}")
            elif helper and s[i] == helper[-1]:
                helper.pop()
            else:
                return False
        if helper:
            return False
        return True