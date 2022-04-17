# https://leetcode.com/problems/valid-parentheses/
## method 1: 77% faster 73 less space
class Solution:
    def isValid(self, s: str) -> bool:
        front = []
        match = {')':'(','}':'{',']':'['}
        for char in s:
            if char in match.values():
                front.append(char)
            elif char in match.keys():
                if len(front)>0 and front[-1] == match[char]:
                    ront = front.pop()
                else:
                    return False
        return front == []
ob = Solution()
example =  "(]"
print(ob.isValid(example))
