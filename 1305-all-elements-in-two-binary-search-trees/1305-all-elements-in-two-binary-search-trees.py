# mrasimzahid.github.io

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def __init__(self, ans=[]):
#         self.ans = ans
        
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

#         def deep(root):
#             if root.left is None and root.right is None:
#                 self.ans.append(root.val)
#                 return
#             if root.left and root.right:
#                 self.ans.append(root.val)
            
#             if root.left:
#                 deep(root.left)
#             if root.right:
#                 deep(root.right)
#         deep(root1)
#         deep(root2)
#         data = self.ans
#         self.ans = []
#         return sorted(data)