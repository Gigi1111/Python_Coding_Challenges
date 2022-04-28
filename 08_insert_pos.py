# https://leetcode.com/problems/search-insert-position/submissions/
## method 1: 
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r =  len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if mid == 0 or nums[mid-1] < target:
                    return mid
                else:
                    r = mid - 1
            elif target > nums[mid]:
                if mid == len(nums)-1:
                    return mid + 1
                else:
                    l = mid + 1
