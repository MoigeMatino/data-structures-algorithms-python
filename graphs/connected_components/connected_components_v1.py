def connected_components_count(graph):
    """
    Counts the number of connected components in an undirected graph.

    Args:
        graph (dict): A dictionary representing the undirected graph where keys are nodes and values are lists of neighboring nodes.

    Returns:
        int: The number of connected components in the graph.

    """
    visited = set()  # Set to store visited nodes
    count = 0  # Counter for connected components
    
    for node in graph:  # Iterate over each node in the graph
        if explore(graph, node, visited) == True:  # Explore the node if it's not visited
            count += 1  # Increment count if a new connected component is found
        
    return count  # Return the count of connected components

def explore(graph, current, visited):
    """
    Explores a node and its neighbors to find connected components using Depth-First Search (DFS).

    Args:
        graph (dict): A dictionary representing the undirected graph where keys are nodes and values are lists of neighboring nodes.
        current: The current node being explored.
        visited (set): A set of visited nodes.

    Returns:
        bool: True if the node is part of a new connected component, False otherwise.

    """
    if current in visited:  # If the current node is already visited, return False
        return False

    visited.add(current)  # Mark the current node as visited

    for neighbor in graph[current]:  # Explore neighbors of the current node
        explore(graph, neighbor, visited)  # Recursively explore each neighbor
        
    return True  # Return True indicating a new connected component is found

"""
Time Complexity Analysis:
- Exploring each edge in the graph: O(e), where e is the number of edges.
Overall: O(e)

Space Complexity Analysis:
- Storing visited nodes: O(n), where n is the number of nodes.
Overall: O(n)

Further Notes:
This algorithm utilizes a Depth-First Search (DFS) approach to find connected components in an undirected graph. 
It iterates over each node in the graph and explores each unvisited node and its neighbors recursively. 
If a new connected component is discovered during exploration, the count is incremented. The time complexity 
is O(e), where e is the number of edges in the graph, and the space complexity is O(n), where n is the 
number of nodes in the graph.
"""
