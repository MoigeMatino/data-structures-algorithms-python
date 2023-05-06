def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B, set())

def build_graph(edges):
    graph = {}
    
    for edge in edges:
        a, b = edge
        
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        
        graph[a].append(b)
        graph[b].append(a)
        
    return graph
    
def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    
    if src in visited:
        return False
    
    visited.add(src)
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst, visited) == True:
            return True
        
    return False

"""
depth first recursive

n = number of nodes
e = number edges
Time: O(e)
Space: O(e)

"""
    
