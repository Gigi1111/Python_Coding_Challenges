# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/
# method1: 76% 48%
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         # turn to list then sort
#         tree_list = []
#         def traverse_tree(cur):
#             if cur:
#                 tree_list.append(cur.val)
#                 traverse_tree(cur.left)
#                 traverse_tree(cur.right)
#
#         traverse_tree(root)
#         tree_list.sort()
#         return tree_list[k-1]
### method 2: O(n), O(n)
# class Solution:
#     def kthSmallest(self, root, k):
#         def inorder(r):
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []
#
#         return inorder(root)[k - 1]
### method 3: O(log N) or O(N) if all are on left, and O(log n)
class Solution:
    def kthSmallest(self, root, k):
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
ob = Solution()
example = TreeNode([5,1,7])
print(ob.kthSmallest(example))
