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
    
    def dfs(node):
        """
        Depth-First Search (DFS) function to explore connected components starting from a given node.

        Args:
            node: The starting node for DFS exploration.

        """
        visited.add(node)  # Mark the current node as visited
        for neighbor in graph[node]:  # Explore neighbors of the current node
            if neighbor not in visited:  # If the neighbor is not visited, recursively explore it
                dfs(neighbor)
    
    for node in graph:  # Iterate over each node in the graph
        if node not in visited:  # If the node is not visited, explore it and its connected component
            dfs(node)
            count += 1  # Increment count for each new connected component
        
    return count  # Return the count of connected components

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
