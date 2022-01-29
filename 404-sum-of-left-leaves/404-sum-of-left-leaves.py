# mrasimzahid.github.io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def depth(root, flag):
            if root is None:
                return 0
            if not root.left and not root.right:
                if flag:
                    return root.val
                else:
                    return 0                
            return depth(root.left, True) + depth(root.right, False)
        return depth(root, False)
