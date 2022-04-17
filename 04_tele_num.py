# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
## method 1:
import string
class Solution:
    def letterCombinations(self, digits):
        look_up =  {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
             '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        if digits == []: return []
        result = []
        def bfs(pos, s):
            if pos == len(digits):
                print('r:',result,'s:',s)
                result.append(s)
            else:
                letters = look_up[digits[pos]]
                print(':- ',letters)
                for letter in letters:
                    print('p:',pos+1,'s+le:',s+letter)
                    bfs(pos+1,s+letter)
                    print(result)

        bfs(0,"")
        return result


ob = Solution()
example = "23"
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(ob.letterCombinations(example))
