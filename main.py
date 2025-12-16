import networkx as nx
import matplotlib.pyplot as plt

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

# Green line (Syretsko-Pecherska) – 23 stations
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

