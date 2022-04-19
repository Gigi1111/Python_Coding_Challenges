# https://leetcode.com/problems/longest-common-prefix/
## method 1: 89% 52%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs[1:]:
            for l in range(len(prefix),-1,-1):
                # print('pre:',prefix[:l])
                if prefix[:l] == str[:l]:
                    break
            if l == 0:
                return ''
            prefix = prefix[:l]

        return prefix

## method 2: 63, 52%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for chars in zip(*strs): # zip + *(return individual ele) turns ['ab','cd'] to [(a,c),(b,d)]
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break

        return prefix
## method 3: fastest 98% 13%
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        if len(strs)==0:
            return prefix

        for i in range(len(min(strs))):
            c=strs[0][i]
            if all(a[i] == c for a in strs):
                # all([1,True,False]) = False, check if all is True
                prefix += c
            else:
                break

        return prefix
