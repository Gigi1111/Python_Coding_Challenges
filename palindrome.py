# https://leetcode.com/problems/valid-palindrome-ii/submissions/

## method 1 : faster than 16%, space 10%
# def validPalindrome(s: str) -> bool:
#     s_backwards = s[::-1]
#
#     if s == s_backwards:
#         return True
#
#     first_diff = [i for i in range(len(s)) if s[i] != s_backwards[i]][0]
#
#     delete_backwards = s_backwards[:first_diff] + s_backwards[first_diff+1:]
#     if delete_backwards == delete_backwards[::-1]:
#         return True
#     delete_s = s[:first_diff] + s[first_diff+1:]
#     if delete_s == delete_s[::-1]:
#         return True
#
#     return False

## method 2: 65% , 52% (BEST)
def validPalindrome(s: str) -> bool:
    def check_palindrome(s,front,back):
        while front < back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1

        return True

    front = 0
    back = len(s) - 1
    while front < back:
        if s[front] != s[back]:
            # remove one char from first half
            return check_palindrome(s,front+1,back) or check_palindrome(s,front,back-1)

        front += 1
        back -= 1

    return True

## method 3: cleaner method 2 (but slower, 52%)
# def validPalindrome(s: str) -> bool:
#     def check_palindrome(s,front,back):
#         while front < back:
#             if s[front] != s[back]:
#                 return [front,back]
#             front += 1
#             back -= 1
#
#         return []
#
#     front = 0
#     back = len(s) - 1
#
#     result = check_palindrome(s,front, back)
#     if result == []:
#         return True
#
#     return check_palindrome(s,result[0]+1,result[1])==[] or check_palindrome(s,result[0],result[1]-1)==[]

print(validPalindrome('aba'))
print(validPalindrome('abac'))
print(validPalindrome('abca'))
print(validPalindrome('caba'))
print(validPalindrome('cac'))
print(validPalindrome('deeee'))
