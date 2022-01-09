# mrasimzahid.github.io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if no root
        if root is None:
            return 0
        # if leaf node
        if root.left == None and root.right == None:
            return 1
        # if no left leaf
        if not root.left:
            return 1 + self.minDepth(root.right)
        # if no right leaf
        elif not root.right:
            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))