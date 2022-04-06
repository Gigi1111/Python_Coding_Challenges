# https://leetcode.com/problems/roman-to-integer/
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
## method 1: 84%, 80%
def romanToInt(s):
    roman_two = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    roman_one = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    num = i = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman_two:
            num += roman_two[s[i:i+2]]
            i += 1
        elif s[i] in roman_one:
            num += roman_one[s[i]]

        i += 1

    return num


print(romanToInt('IV'))
print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
