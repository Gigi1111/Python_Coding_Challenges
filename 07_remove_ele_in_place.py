# https://leetcode.com/problems/remove-element/submissions/
## method 1:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if val not in nums:
            return len(nums)
        cur = 0
        n = len(nums)
        while cur < n:
            if nums[cur] == val:
                # swap the current ele that is val with the last element 
                nums[cur] = nums[n-1]
                n -= 1     
            # only move on to next ele when the swapped ele isn't val
            else:
                cur += 1
                   
        return n
        
## method 2:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
            count = 0
            for i in range(len(nums)):
                if nums[i] != val :
                    nums[count] = nums[i]
                    count +=1
                print(nums, i, count)
            return count
