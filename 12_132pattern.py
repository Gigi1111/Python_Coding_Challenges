import math
class Solution:
    # time limit exceeded
    def find132pattern_v1(self, nums) -> bool:
        # j, k must > i, but k < j 
        for i in range(len(nums)-2):
            print(f"i:{i},nums[i]:{nums[i]}, max(nums[i+1:]):{max(nums[i+1:])}, cond 1:{nums[i]>0 and nums[i]==nums[i-1]}, cond 2:{nums[i] >= max(nums[i+1:])-1}")
            if (i>0 and nums[i]==nums[i-1]) or nums[i] >= max(nums[i+1:])-1: continue
            for j in range(i+1, len(nums)-1):
                print(f"j:{j},nums[j]:{nums[j]}")
                if nums[j] == nums[j-1] or nums[j] <= nums[i]+1 : continue
                elif nums[j] > nums[i] and any([nums[i]<x<nums[j] for x in nums[j+1:]]): return True

        return False

    # too slow, has to break it down
    def find132pattern_v2(self, nums) -> bool:
        if len(nums) < 3: return False
        for i in range(1,len(nums)-1):
            if nums[i] <= min(nums[:i]) or nums[i] <= min(nums[i+1:]): continue
            elif any([min(nums[:i]) < x < nums[i] for x in nums[i+1:]]): return True

        return False

    # too slow
    def find132pattern_v3(self, nums) -> bool:
        minSofar = {}
        leftMin = math.inf
        for i in range(len(nums)):
            leftMin = min(leftMin, nums[i])
            minSofar[i] = leftMin
        
        for i in range(len(nums)-2,-1,-1):
            for x in nums[i+1:]:
                if minSofar[i] < x < nums[i]:
                    return True

        return False

    def find132pattern_v4(self, nums) -> bool:
        minSofar = {}
        leftMin = math.inf
        for i in range(len(nums)):
            leftMin = min(leftMin, nums[i])
            minSofar[i] = leftMin
        
        rightMaxSmaller, stack = {}, []
        # get the max on right hand side that's smaller than nums[i]
        # O(nlogn) 
        for i in range(len(nums)-1,-1,-1): # enumerate(nums[::-1]):
            tmp = math.inf # if nothing on the right is smaller than nums[i], store super large value
            while stack and stack[-1] < nums[i]:
                tmp = stack.pop()
            stack.append(nums[i])
            rightMaxSmaller[i] = tmp
        
        for i in range(len(nums)):
            if minSofar[i] < rightMaxSmaller[i] < nums[i]: return True

        return False

    # FASTEST AND LEAST SPACE
    def find132pattern(self, nums) -> bool:
        if len(nums)<3:
            return False
      
        second_num = -math.inf
        stck = []
        # Try to find nums[i] < second_num < stck[-1]
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second_num:
                return True
            # always ensure stack can be popped in increasing order
            while stck and stck[-1] < nums[i]:
                second_num = stck.pop()  # this will ensure  second_num < stck[-1] for next iteration

            stck.append(nums[i])
        return False

obj = Solution()
tests = [[1,2,3,4],[-1,1,3,1,4,2,1,0],[-1,3,2,0],[1,3,2,4,5,6,7,8,9,10],[1,3,2,1,1],[-2,1,2,-2,1,2]]
print([obj.find132pattern(test) for test in tests])
