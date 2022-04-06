# https://leetcode.com/problems/integer-to-roman/
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
## method 1:
def intToRoman(num):
    roman_symbols = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    i = 1
    roman = ''
    while i <= len(str(num)):
        digit = num % 10**i
        if digit in list(roman_symbols.values()):
            roman = list(roman_symbols.keys())[list(roman_symbols.values()).index(digit)] + roman
            num -= digit
        else:
            add_roman = ""
            if digit >= 10**i/2:
                add_roman = list(roman_symbols.keys())[list(roman_symbols.values()).index(10**i/2)]
                num -= 10**i/2
                digit -= 10**i/2
            while digit > 0:
                add_roman += list(roman_symbols.keys())[list(roman_symbols.values()).index(10**(i-1))]
                num -= 10**(i-1)
                digit -= 10**(i-1)
            roman = add_roman + roman

        i+=1

    return roman

print(intToRoman(6))
print(intToRoman(4))
# # print(romanToInt('IV'))
# # print(romanToInt('III'))
print(intToRoman(58))
print(intToRoman(49))
# # print(romanToInt('LVIII'))
print(intToRoman(1994))
# # print(romanToInt('MCMXCIV'))

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
