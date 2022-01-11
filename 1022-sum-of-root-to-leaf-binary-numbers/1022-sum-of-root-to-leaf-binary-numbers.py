# mrasimzahid.github.io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        left = right = []
        if root.left == None and root.right == None:
            return str(root.val)
        if root.right != None:
            right = self.helper(root.right)
            right = [str(root.val) + each for each in right]
        if root.left != None:
            left = self.helper(root.left)
            left = [str(root.val) + each for each in left]
        return left + right

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
            result = self.helper(root)
            return sum([int(each_final, 2) for each_final in result])
            