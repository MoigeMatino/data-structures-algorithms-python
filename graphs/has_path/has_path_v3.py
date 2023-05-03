def has_path(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True
        
    return False

"""
depth first

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)

"""

    
