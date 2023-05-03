def has_path(graph, src, dst):
    stack = [src]
    
    while stack:
        current = stack.pop()
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            stack.append(neighbor)
        
    return False

"""
Depth first - iterative

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)

"""