# https://leetcode.com/problems/generate-parentheses/solution/
## method 1: 77% 79%
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def generate(s=[], left = 0, right = 0):
            if left == right and left == n:
                ans.append("".join(s))
                return
            if len(s) == 0 or left < n:
                s.append('(')
                generate(s,left+1,right)
                # print('1.s:',s,'ans:',ans)
                s.pop() # to backtrack to try other combinations
                # print('3.s:',s,'ans:',ans)
            if right < left:
                s.append(')')
                generate(s,left,right+1)
                # print('2.s:',s,'ans:',ans)
                s.pop() # to backtrack to try other combinations
                # print('4.s:',s,'ans:',ans)

        generate()

        return ans
