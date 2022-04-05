# ## method 1: 66% faster 18% less space
# def reverse(x):
#     neg = False
#     x_str = str(x)
#     if x_str[0] == '-':
#         neg = True
#         x_str = x_str[1:]
#
#     reverse = int(x_str[::-1])
#     if neg:
#         reverse = -int(x_str[::-1])
#
#     if (reverse > (2**31)-1) or (reverse < -(2**31)):
#         reverse = 0
#
#     return reverse
# ## method 2: 85%, 67%
# def reverse(x):
#     if (x >= (2**31)-1) or (x <= -(2**31)):
#         return 0
#     else:
#         x_str = str(x)
#         if x >= 0:
#             reverse = x_str[::-1]
#         else:
#             reverse = "-" + x_str[:0:-1] # end (inclusive) to 0 (exclusive)
#         reverse = int(reverse)
#         if reverse >= (2**31)-1 or reverse <= -(2**31):
#             return 0
#
#         return reverse
## method 3:
def reverse(x):
    if (x >= (2**31)-1) or (x <= -(2**31)):
        return 0

    reverse = int(str(abs(x))[::-1])

    if reverse >= (2**31)-1:
        return 0

    return reverse if x > 0 else (-reverse)

reverse(123)
reverse(-123)
reverse(120)
reverse(1534236469)
