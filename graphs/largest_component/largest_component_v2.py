def largest_component(graph):
    max = 0
    visited = set()
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > max:
            max = size
        
    return max

def explore_size(graph, node, visited):
    stack = [node]
    size = 0
    
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        
        size += 1
        visited.add(current)
        
        for neighbor in graph[current]:
            stack.append(neighbor)
        
    return size

"""
Depth first iterative approach

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)

"""