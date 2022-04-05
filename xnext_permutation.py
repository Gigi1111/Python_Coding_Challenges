def nextPermutation(nums):
    nums_sorted = nums.copy()
    nums_sorted.sort()
    print(nums_sorted)


nums = [2,3,1]
nextPermutation(nums)
print(nums)
