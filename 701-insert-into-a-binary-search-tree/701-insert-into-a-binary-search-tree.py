# mrasimzahid.github.io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, val):
        if root:
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                    return
                else:
                    self.helper(root.left, val)
            elif root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                    return 
                else: 
                    self.helper(root.right, val)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        self.helper(root, val)
        return root
