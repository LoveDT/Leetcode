class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        result = []
        helper = ''
        helpermap = {}
        for element in strs:
            helper = ''.join(sorted(element))
            if hash(helper) not in helpermap:
                helpermap[hash(helper)] = []
            helpermap[hash(helper)].append(element)
        brackets = helpermap.keys()
        helper = []
        for i in range(len(brackets)):
            helper = helpermap[brackets[i]]
            if len(helper)!=1:
                for words in helper:
                    result.append(words)
        return result
        