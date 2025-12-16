from collections import deque
import networkx as nx

def bfs_path(graph: nx.Graph, start, goal):
   
    visited = set()    
    queue = deque([[start]])

    while queue:  
        path = queue.popleft()
        node = path[-1] 

        if node == goal:
            return path
        
        elif node not in visited:
            for neighbor in graph.neighbors(node):
                if neighbor not in path:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
            visited.add(node)
    return None
