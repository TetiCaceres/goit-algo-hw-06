import networkx as nx
import matplotlib.pyplot as plt
from BFS import bfs_path
from DFS import dfs_path

# Create a graph representing Kyiv Metro
metro = nx.Graph()

# Red line (Sviatoshynsko–Brovarska) 
red_line = [
     "Akademmistechko", "Zhytomyrska", "Sviatoshyn", "Nyvky", "Beresteiska",
    "Shuliavska", "Politekhnichnyi Instytut", "Vokzalna", "Universytet",
    "Teatralna", "Khreshchatyk", "Arsenalna", "Dnipro", "Hidropark",
    "Livoberezhna", "Darnytsia", "Chernihivska", "Lisova"
]

# Blue line (Obolonsko–Teremkivska) 
blue_line = [
    "Heroiv Dnipra", "Minska", "Obolon", "Pochaina", "Tarasa Shevchenka",
    "Kontraktova Ploshcha", "Poshtova Ploshcha", "Maidan Nezalezhnosti", "Ploshcha Ukrainskykh Heroiv",  
    "Olimpiiska", "Palats Ukraina","Lybidska", "Demiivska", "Holosiivska", "Vasylkivska", "Vystavkovyi Tsentr",
    "Ipodrom", "Teremky"
]

# Green line (Syretsko-Pecherska) 
green_line = [
    "Syrets", "Dorohozhychi", "Lukianivska", "Zoloti Vorota", "Palats Sportu",
    "Klovska", "Pecherska", "Druzhby Narodiv", "Vydubychi", "Slavutych",
    "Osokorky", "Pozniaky", "Kharkivska", "Vyrlytsia", "Boryspilska", "Chervonyi Khutir"
]

# Combine all stations
all_stations = red_line + blue_line + green_line
metro.add_nodes_from(all_stations)

# Edges – Red line connections
red_edges = [(red_line[i], red_line[i+1]) for i in range(len(red_line)-1)]

# Edges – Blue line connections
blue_edges = [(blue_line[i], blue_line[i+1]) for i in range(len(blue_line)-1)]

# Edges – Green line connections
green_edges = [(green_line[i], green_line[i+1]) for i in range(len(green_line)-1)]

interchanges = [
    ("Teatralna", "Zoloti Vorota"),  # Red ↔ Green
    ("Khreshchatyk", "Maidan Nezalezhnosti"),  # Red ↔ Blue
    ("Ploshcha Ukrainskykh Heroiv", "Palats Sportu")  # Blue ↔ Green
]

metro.add_edges_from(red_edges + blue_edges + green_edges + interchanges)

# Plot
plt.figure(figsize=(14,7))
nx.draw(metro, with_labels=True, node_size=700, font_size=8, node_color="skyblue")
plt.title("Kyiv Metro Graph (Accurate Stations & Transfers)")
plt.show()

print("Stations count:", metro.number_of_nodes())
print("Connections count:", metro.number_of_edges())
print("Degrees:", dict(metro.degree()))

# ---------------------------
# Task 2: DFS and BFS
# ---------------------------

# Example paths
start = "Syrets"
goal = "Teremky"

# Find paths using DFS and BFS
dfs_result = dfs_path(metro, start, goal)
bfs_result = bfs_path(metro, start, goal)

# Display results
print("DFS path:", dfs_result)
print("BFS path:", bfs_result)
print("DFS length:", len(dfs_result))
print("BFS length:", len(bfs_result))

# Explanation of differences
if len(dfs_result) > len(bfs_result):
    print("\nDFS (Depth-First Search) is exploring deep into the graph, often visiting unnecessary stations.")
    print("It does not guarantee the shortest path in terms of the number of nodes traversed.")

print("\nBFS (Breadth-First Search) explores all the neighbors of each node level by level,")
print("so it always guarantees the shortest path by the number of edges between start and goal.")
