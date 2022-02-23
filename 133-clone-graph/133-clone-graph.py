# mrasimzahid.github.io

# Technique: Recursive, DFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.cache = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        if node in self.cache:
            return self.cache[node]
        
        self.cache[node] = Node(node.val)
        self.cache[node].neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        
        return self.cache[node]