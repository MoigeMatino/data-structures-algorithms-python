def connected_components_count(graph):
    visited = set()
    count = 0
    
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
        
    return count
        
        
def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
        
    return True

"""
depth first - recursive

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)

This algorithm can be broken down into two functions:
1. Function to iterate over every node in the graph so 
    as to start a traversal from each of those nodes.

2. Function that traverses the current node in the graph 
    and explores it to find the number of nodes connected 
    to it to make a connected component.

Note that the base case in the recursive function is implicit.
i.e by virtue of line 18: 'for neighbor in graph[current]', it 
implies that the recursive call will only be made if the current
node has neighbor. In the event that the neighbor is absent, the 
recursive call is not made; the base case is the absence of a recursive
call/case.

"""
