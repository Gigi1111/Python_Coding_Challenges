# https://leetcode.com/problems/first-missing-positive/submissions/
## correct method of time O(n) and constant space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        isOne = False
        for i, val in enumerate(nums):
            if val == 1: 
                isOne = True
            if val <= 0 or val > len(nums):
                nums[i] = 1
            
        if not isOne: return 1
        
        # make the number that's present in list's index negative so we know it's present
        for i, val in enumerate(nums):
            # get the index of that number that should be present, i.e. [3..] means nums[2] should be neg to show it's present
            present_index = abs(val) - 1
            # only make it neg if it's still pos cuz there can be duplicates
            if nums[present_index] > 0:
                nums[present_index] *= -1
            
        for i, val in enumerate(nums):
            if val > 0:
                return i+1
            
        return len(nums) + 1
## method 2:  time O(n.logn), space constant
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort() # O(n.logn)
        
        prev = 0
        last = -1
        for i, val in enumerate(nums):
            if val <= 0: 
                continue
                
            if (i == 0 and val > 0) or (i > 0 and val > 0 and nums[i-1] != val):    
                prev += 1
            
            if val > prev:
                return prev
                
        return nums[-1] + 1 if nums[-1] > 0 else 1
