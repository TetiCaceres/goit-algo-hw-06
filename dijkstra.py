import networkx as nx

def dijkstra(graph: nx.Graph, start):
    distances = {v: float("infinity") for v in graph.nodes}
    previous = {v: None for v in graph.nodes}

    distances[start] = 0 
    unvisited = list(graph.nodes)

    while unvisited:
        # Vertex with smallest distance
        current = min(unvisited, key=lambda v: distances[v])

        if distances[current] == float('infinity'):
            break

        for neighbor in graph.neighbors(current):
            weight = graph[current][neighbor].get("weight", 1)
            new_distance = distances[current] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

        unvisited.remove(current
                         )
    return distances, previous

def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path if path[0] == start else []






