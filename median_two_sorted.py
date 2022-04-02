# https://leetcode.com/problems/median-of-two-sorted-arrays/
## method 1: 84% 71%
def findMedianSortedArrays(nums1, nums2) -> float:
    n3 = []
    i1 = i2 = 0
    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] <= nums2[i2]:
            n3.append(nums1[i1])
            i1 += 1
        elif nums1[i1] > nums2[i2]:
            n3.append(nums2[i2])
            i2 += 1

    if i1 < len(nums1):
        n3 += nums1[i1:]
    elif i2 < len(nums2):
        n3 += nums2[i2:]

    if len(n3) % 2 != 0:
        return n3[int(len(n3)/2)]

    return (n3[int(len(n3)/2)-1] + n3[int(len(n3)/2)])/2


# nums1 = [1,3], nums2 = [2]
nums1 = [1,3]
nums2 = [2]
print(findMedianSortedArrays(nums1,nums2))
