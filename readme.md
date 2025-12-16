# Kyiv Metro Graph Analysis 

## 1. Graph Creation

- The graph represents **Kyiv Metro** with three lines:
  - **Red line (Sviatoshynsko–Brovarska)**
  - **Blue line (Obolonsko–Teremkivska)**
  - **Green line (Syretsko–Pecherska)**
- **Nodes**: metro stations
- **Edges**: connections between adjacent stations and interchanges between lines
- **Total stations**: 52
- **Total connections**: 52

The graph was visualized using NetworkX and Matplotlib.

---

## 2. Graph Characteristics

- Degree of each station was calculated.  
  - Most stations have **degree 2** (connected to previous and next station).  
  - **Interchange stations** have higher degrees (3), e.g., `Teatralna`, `Khreshchatyk`, `Ploshcha Ukrainskykh Heroiv`.

---

## 3. Pathfinding using DFS and BFS

- **Start node**: `Syrets`  
- **Goal node**: `Teremky`

### DFS (Depth-First Search)
- DFS explores **deep paths** first.  
- May produce a longer route if multiple branches exist.  
- In our graph, the DFS path:  
'Syrets' → 'Dorohozhychi' → 'Lukianivska' → 'Zoloti Vorota' → 'Palats Sportu' → 'Ploshcha Ukrainskykh Heroiv' → 'Olimpiiska' → 'Palats Ukraina' → 'Lybidska' → 'Demiivska' → 'Holosiivska' → 'Vasylkivska' → 'Vystavkovyi Tsentr' → 'Ipodrom' → 'Teremky'

### BFS (Breadth-First Search)
- BFS explores **neighbors level by level**.  
- Always guarantees the **shortest path by number of stations**.  
- In our graph, the BFS path:
'Syrets' → 'Dorohozhychi' → 'Lukianivska' → 'Zoloti Vorota' → 'Palats Sportu' → 'Ploshcha Ukrainskykh Heroiv' → 'Olimpiiska' → 'Palats Ukraina' → 'Lybidska' → 'Demiivska' → 'Holosiivska' → 'Vasylkivska' → 'Vystavkovyi Tsentr' → 'Ipodrom' → 'Teremky'


### Comparison
- Both DFS and BFS returned **the same path**.
- **Reason**: the graph structure between Syrets and Teremky is linear along the green line with no alternative shorter branches.  
- DFS could have returned a longer path if the graph had more branching.

---

## 4. Conclusions

1. **DFS vs BFS**
   - DFS is useful for exploring all paths and understanding graph structure.
   - BFS is optimal for finding the shortest path in terms of edges.

2. **Graph Analysis**
   - Interchange stations have higher connectivity.
   - Linear structure of metro lines simplifies pathfinding for certain start and goal nodes.

3. **Observation**
   - Even when DFS and BFS produce the same path, their **search strategies differ**, which is important for more complex networks.

---


