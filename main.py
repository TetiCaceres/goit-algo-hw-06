import networkx as nx
import matplotlib.pyplot as plt
from BFS import bfs_path
from DFS import dfs_path
from dijkstra import dijkstra, get_path

# =======================
# Helper function
# =======================
def print_header(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# =======================
# TASK 1: Kyiv Metro Graph
# =======================

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


# Add edges (2 min travel per station)
for line in [red_line, blue_line, green_line]:
    for i in range(len(line) - 1):
        metro.add_edge(line[i], line[i+1], weight=2)

# Interchanges (longer time – 5 minutes)
interchanges = [
    ("Teatralna", "Zoloti Vorota", 5),           # Red ↔ Green
    ("Khreshchatyk", "Maidan Nezalezhnosti", 5), # Red ↔ Blue
    ("Ploshcha Ukrainskykh Heroiv", "Palats Sportu", 5)  # Blue ↔ Green
]

for u, v, w in interchanges:
    metro.add_edge(u, v, weight=w)

# Plot
plt.figure(figsize=(14,7))
nx.draw(metro, with_labels=True, node_size=700, font_size=8, node_color="skyblue")
plt.title("Kyiv Metro Graph (Accurate Stations & Transfers)")
plt.show()


# Graph info
print_header("TASK 1: GRAPH ANALYSIS")
print(f"Total stations: {metro.number_of_nodes()}")
print(f"Total connections: {metro.number_of_edges()}")
print("\nStations degree (connections count):")
for station, degree in metro.degree():
    print(f"  - {station}: {degree}")

# ---------------------------
# Task 2: DFS and BFS
# ---------------------------

# Example paths
start = "Syrets"
goal = "Teremky"

# Find paths using DFS and BFS
dfs_result = dfs_path(metro, start, goal)
bfs_result = bfs_path(metro, start, goal)

print_header("TASK 2: DFS vs BFS PATH SEARCH")
print(f"Start station: {start}")
print(f"End station:   {goal}")

print("\nDFS result:")
print(" → ".join(dfs_result))
print(f"Stations count: {len(dfs_result)}")

print("\nBFS result:")
print(" → ".join(bfs_result))
print(f"Stations count: {len(bfs_result)}")

print("\nExplanation:")
print(
    "DFS explores one branch deeply and does not guarantee the shortest path.\n"
    "BFS explores level by level and guarantees the shortest path by number of stations."
)

# ---------------------------
# Task 3: Dijkstra Algorithm
# ---------------------------

print_header("TASK 3: DIJKSTRA SHORTEST PATH (BY TIME)")

start_station = "Syrets"
target_stations = ["Teremky", "Lisova", "Akademmistechko"]


distances, previous = dijkstra(metro, start_station)

print(f"Start station: {start_station}")

for target in target_stations:
    path = get_path(previous, start_station, target)
    time = distances[target]

    print("\nDestination:", target)
    print("Route:", " → ".join(path))
    print(f"Travel time: {time} minutes")