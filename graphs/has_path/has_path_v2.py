from collections import deque

def has_path(graph, src, dst):
    queue = deque([ src ])
    
    while queue:
        current = queue.popleft()
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
        
    return False

"""
Breadth first 

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)

"""