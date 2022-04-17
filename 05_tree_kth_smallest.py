# https://leetcode.com/problems/increasing-order-search-tree/
## method 1:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root):
        #  def inorder(node):
        #     if node:
        #         inorder(node.left)
        #         node.left = None
        #         self.cur.right = node
        #         self.cur = node
        #         inorder(node.right)
        #
        # ans = TreeNode(None)
        # self.cur = TreeNode(None)
        # inorder(root)
        # return ans.right
        return root.left

ob = Solution()
example = TreeNode([5,1,7])
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
print(ob.increasingBST(example))
