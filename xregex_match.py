# https://leetcode.com/problems/regular-expression-matching/
# ## method 1:
# def isMatch(s,p):
#     pattern = ""
#     i1, i2 = 0, 0
#     while i1 < len(s) and i2 < len(p):
#         if p[i2] not in ['.','*'] and s[i1] != p[i2]:
#             return False
#         elif s[i1] == p[i2]:
#             i1 += 1
#             i2 += 1
#         elif p[i2] == '.':
#             pattern = s[i1]
#             i1 += 1
#             i2 += 1
#         elif p[i2] == '*' and pattern == s[i1]:
#             i1 += 1
#
#
#     return i1 == len(s) and i2 == len(s)
## method 1:
def isMatch(s,p):
    pattern = ""
    i1, i2 = 0, 0
    while i1 < len(s) and i2 < len(p):
        print('i1:',i1,'i2:',i2,'s:',s[i1],', p:',p[i2],", pattern;",pattern)
        if s[i1] == p[i2]:
            pattern = s[i1]
            i1 += 1
            i2 += 1
        elif p[i2] == '.':
            pattern = '.'
            i1 += 1
            i2 += 1
        elif p[i2] == '*' and (pattern == '.' or pattern == s[i1]):
            i1 += 1
        else:
            return False

    return i1 == len(s)




s = "aa"
# p = "a"
# p = "a*"
s = "ab"
p = ".*"
s = "aab"
p = "c*a*b"
print(isMatch(s,p))
