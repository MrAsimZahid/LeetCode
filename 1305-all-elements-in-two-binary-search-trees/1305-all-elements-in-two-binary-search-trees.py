# mrasimzahid.github.io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        values = []
        def collect(root):
            if root:
                collect(root.left)
                values.append(root.val)
                collect(root.right)
        collect(root1)
        collect(root2)
        return sorted(values)

