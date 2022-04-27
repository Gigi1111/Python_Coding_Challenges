# https://leetcode.com/problems/implement-strstr/submissions/
## method 1: O(n), O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if needle == '': return 0
        # return haystack.index(needle)
        
        if needle == '': return 0
        
        for i in range(len(haystack)-(len(needle)-1)):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1