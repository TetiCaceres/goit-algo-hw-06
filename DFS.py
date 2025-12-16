import networkx as nx

def dfs_path(graph: nx.Graph , start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None
            