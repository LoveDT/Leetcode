class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        if len(pattern) == 0 and len(str) == 0:
            return True
        if len(pattern) == 0 or len(str) == 0:
            return False
        strlist = []
        word = []
        for i in range(len(str)):
            if str[i] == ' ':
                tmp = ''.join(word)
                word = []
                strlist.append(tmp)
            else:
                word.append(str[i])
        tmp = ''.join(word)
        strlist.append(tmp)
        if len(strlist) != len(pattern):
            return False
        patternhelper = {}
        strhelper = {}
        for i in range(len(pattern)):
            if pattern[i] not in patternhelper and strlist[i] not in strhelper:
                patternhelper[pattern[i]] = strlist[i]
                strhelper[strlist[i]] = pattern[i]
            elif pattern[i] in patternhelper and strlist[i] != patternhelper[pattern[i]]:
                return False
                
            elif strlist[i] in strhelper and pattern[i] != strhelper[strlist[i]]:
                return False
        return True
        