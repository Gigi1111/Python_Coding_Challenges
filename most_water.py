# https://leetcode.com/problems/container-with-most-water/
# ## method 1: wrong becuz should think of it as left right index converging
# def maxArea(height):
#     most_water = 0
#     for i, left in enumerate(height):
#         for j in range(i,len(height)):
#             right = height[j]
#             if left >= right:
#                 temp = (j - i) * right
#             else:
#                 temp = (j - i) * left
#             if temp > most_water:
#                 most_water = temp
#     return most_water
## move l or r to find higher wall
## method 2:
def maxArea(height):
    l, r, most_water = 0, len(height)-1, 0
    while l < r:
        most_water = max((r-l)*min(height[l],height[r]),most_water)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return most_water
# height = [1,1]
height = [1,8,6,2,5,4,8,3,7]
# Output: 49
print(maxArea(height))
