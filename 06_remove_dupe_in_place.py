# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
## method 1:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        for i in range(len(nums)):
            if i+1 < len(nums) and nums[i] == nums[i + 1]:
                continue
            nums[count] = nums[i]
            count += 1
        return count
