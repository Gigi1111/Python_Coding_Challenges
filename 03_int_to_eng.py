# https://leetcode.com/problems/integer-to-english-words/
# 0 <= num <= 231 - 1
# -----------------------------------------------------------------------
# pip install inflect
# https://pypi.org/project/inflect/
## method 1: inflect package (useful for natural language generation, correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words.)
# import inflect
# p = inflect.engine()
# print(p.number_to_words(1234567))
# print(p.number_to_words(22))
# -----------------------------------------------------------------------
## method 2: num2words package (https://pypi.org/project/num2words/)
# pip install num2words
# from num2words import num2words
# print(num2words(42))
# print(num2words(42, to='ordinal'))
# print(num2words(42, lang='fr'))
# -----------------------------------------------------------------------
## method 3: 12% faster, 71% less space
# def numberToWords(num):
#     num2words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
#              6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
#             11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
#             15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
#             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
#             50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
#             90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million',1000000000: 'Billion'}
#     i = 1
#     num_word = ''
#     debug = True
#     if num == 0:
#         return 'Zero'
#     while i <= len(str(num)):
#         if debug:
#             print('----num:',num)
#         over_thousand = "1"
#         if debug:
#             print('i:',i)
#
#         if i < 4:
#             if debug:
#                 print('-2:',str(num)[-2:])
#             if i < 2 and int(str(num)[-2:]) < 20:
#                 digit = int(str(num)[-2:])
#             else:
#                 digit = num % 10**i
#         else:
#             count = 0
#             for d in str(num)[::-1]:
#                 if d != '0':
#                     break
#                 count += 1
#                 if count == 3:
#                     over_thousand += '000'
#                     count = 0
#             if debug:
#                 print('over:',over_thousand)
#
#             base = min(len(str(num)), len(over_thousand)+2)
#             digit = num % 10**base
#
#             digit = int(digit / int(over_thousand))
#
#         over_thousand = int(over_thousand)
#         if debug:
#             print('over_thousand:',over_thousand)
#             print('di:',digit)
#
#         prefix = ''
#
#         if digit > 0 :
#             temp = digit
#             hund = int(temp / 100)
#             if hund > 0:
#                 prefix += num2words[hund] + ' ' + num2words[100] + ' '
#                 temp -= hund * 100
#             if temp < 20 and temp > 0 :
#                 prefix += num2words[temp] + ' '
#                 temp -= temp
#             elif temp > 0:
#                 ten = int(temp / 10)
#                 prefix += num2words[ten*10] + ' '
#                 temp -= ten * 10
#             if temp > 0 and temp < 10:
#                 prefix += num2words[temp] + ' '
#
#             if over_thousand > 1:
#                 prefix += num2words[over_thousand] + ' '
#
#         num_word = prefix + num_word
#         digit *= over_thousand
#         num -= digit
#         if debug:
#             print('num_word:',num_word)
#         i += 1
#     return num_word.rstrip()

## method 4: 93% faster, 96% less space
class Solution:
    num2words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million',1000000000: 'Billion'}

    def numberToWords(self, num):
        if num == 0 : return self.num2words[num]
        num_word = ""
        i = 0
        base_count = 0
        while num > 0:
            if num % 1000 > 0:
                base = ""
                if base_count > 0: base = Solution.num2words[1000**base_count]
                num_word = self.dealWith(num % 1000) + base + ' ' + num_word
            num //= 1000
            base_count += 1

        return num_word.strip() #strip remove leading/training space VS. rstrip: remove trailing (Rightside)

    def dealWith(self, num):
        if num == 0:
            return ''
        elif num < 20:
            return Solution.num2words[num] + ' '
        elif num < 100:
            return Solution.num2words[(num//10) * 10] + ' ' + self.dealWith(num % 10)
        else:
            return Solution.num2words[num//100] + ' ' + Solution.num2words[100] + ' ' + self.dealWith(num % 100)

ob = Solution()
# print(ob.numberToWords(512))
# print(ob.numberToWords(7835271))
print(ob.numberToWords(33000))
