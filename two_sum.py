# https://leetcode.com/problems/two-sum/
# ## method 1: faster 31% , storage 77%
# def twoSum(nums, target):
#     for i, num1 in enumerate(nums):
#         num2 = (target - num1)
#         if num2 in nums[i+1:]:
#             return [i, (nums[i+1:].index(num2)+i+1)]
#
#     return []
## method 2: faster 56% , storage 25%
def twoSum(nums, target):
    checked = {}
    for i, num1 in enumerate(nums):
        num2 = (target - num1)
        if num2 in checked:
            return [i, checked[num2]]
        checked[num1] = i
    return []

print(twoSum([2,7,11,15],9))
print(twoSum([3,3],6))
print(twoSum([3,2,4],6))
