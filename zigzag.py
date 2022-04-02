# https://leetcode.com/problems/zigzag-conversion/solution/
## method 1
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    n = len(s)
    cycle = 2*numRows - 2
    strlist = []
    for i in range(numRows):
        for j in range(i, n, cycle):
            strlist.append(s[j])
            if i != numRows-1 and i != 0 and j+cycle-2*i < n:
                strlist.append(s[j+cycle-2*i])
    newstr = ''.join(strlist)
    return newstr


# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 0,6         (4,2)numRows + numRows - 2
# 1,4,2,4,2
# 2,2,4,2
#3,6
# 0     6      12
# 1   5 7   11 13
# 2 4   8 10
# 3     9
s = "PAYPALISHIRING"
print(convert(s,4))
# P   A   H   N
# A P L S I I G
# Y   I   R
# 2 1
