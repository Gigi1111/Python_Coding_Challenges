# https://leetcode.com/problems/longest-substring-without-repeating-characters/
## method 1: 33%, 16%
# def lengthOfLongestSubstring(s: str):
#     temp = ""
#     substring = ""
#
#     for i, char in enumerate(s):
#         if char not in temp:
#             temp += char
#         else:
#             if len(temp) > len(substring):
#                 substring = temp
#             last_index = len(temp) - temp[::-1].index(char)
#             temp = temp[last_index:] + char
#         print(temp)
#
#     if len(temp) > len(substring):
#         substring = temp
#     return len(substring)
## method 2: 79%, 16%
def lengthOfLongestSubstring(s: str):
    dicts = {}
    maxlength = start = 0
    for i,value in enumerate(s):
        if value in dicts:
            sums = dicts[value] + 1
            if sums > start:
                start = sums
        num = i - start + 1
        if num > maxlength:
            maxlength = num
        dicts[value] = i
        print(dicts)
    return maxlength

s = "abcabcbb"
# Output: 3
print(lengthOfLongestSubstring(s))
