class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        length = len(s)
        sourcemap,targetmap = dict(),dict()
        for i in range(length):
            source,target = sourcemap.get(t[i]),targetmap.get(s[i])
            if source is None and target is None:
                sourcemap[t[i]] = s[i]
                targetmap[s[i]] = t[i]
            elif source!=s[i] or target!=t[i]:
                return False
        return True
        
        