def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

def build_graph(edges):
    graph = {}
    for edge in edges:
        a,b = edge
        
        if a not in graph:
            graph[a] = []
        
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
        
    return graph

def has_path(graph, src, dst, visited):
    stack = [src]
    
    while stack:
        current = stack.pop()
        
        if current == dst:
            return True
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for neighbor in graph[current]:
            stack.append(neighbor)
        
    return False
    
"""
Depth first iterative

n = number of nodes
e = number edges
Time: O(e)
Space: O(e)

NB: In this problem, it is very important to account for the presence of cycles with is a relevant/possible occurrence
with undirected graphs. This keeps us from being trapped in an infinite loop.

"""
