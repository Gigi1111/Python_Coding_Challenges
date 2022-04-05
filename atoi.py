# https://leetcode.com/problems/string-to-integer-atoi/submissions/
## method 1: 78% faster, 33% less space
def myAtoi(s):
    num_str = []
    for i, char in enumerate(s):
        if (char in ['+','-'] and i < len(s)-1 and s[i+1].isdigit() and num_str == []) or char.isdigit():
            num_str.append(char)
        elif num_str == [] and not char == ' ':
            break
        elif len(num_str) > 0 and not char.isdigit():
            break

    if num_str == [] or num_str in ['+','-']:
        return 0

    num = int(''.join(num_str))

    return min(num, 2**31-1) if num >= 0 else max(num, -2**31)


# s = "42"
s = "   +42 daf"
# s = "   -42"
# s = "4193 with words"
# s = "words and 987"
s = "+-12"
s="00000-42a1234"
print(myAtoi(s))
