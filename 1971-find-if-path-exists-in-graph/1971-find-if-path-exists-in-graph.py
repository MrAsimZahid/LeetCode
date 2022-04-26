# mrasimzahid.github.io

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        queue = deque()
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        print(graph)
        queue.append(source)
        visited = set()
        while queue:
            current_node = queue.popleft()
            if current_node == destination:
                return True
            visited.add(current_node)
            print(graph[current_node])
            for neighbour in graph[current_node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    
        return False
    
    
    
    
#     def helper(self, source, destination, edges, visited):
#         visited += source
#         dest = []
#         for edge in edges:
#             if edge[0] in source and edge[0] not in visited:
#                 dest.append(edge[1])
#             elif edge[1] in source and edge[1] not in visited:
#                 dest.append(edge[0])
#         if not dest:
#             return False
#         if destination in dest:
#             return True
#         else:
#             source = dest
#             return self.helper(source, destination, edges, visited)

#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         if not edges and n == 1:
#             return True
#         visited = []
#         return self.helper([source], destination, edges, visited) 