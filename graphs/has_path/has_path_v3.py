def has_path(graph, src, dst):
    """
    Checks if there is a path between two nodes in a graph using Depth-First Search (DFS).

    Args:
        graph (dict): A dictionary representing the graph where keys are nodes and values are lists of neighboring nodes.
        src: The source node.
        dst: The destination node.

    Returns:
        bool: True if there is a path from src to dst, False otherwise.

    """
    if src == dst:  # If source and destination are the same, return True
        return True
    
    for neighbor in graph[src]:  # Explore neighbors of the source node
        if has_path(graph, neighbor, dst) == True:  # Recursively check for a path from neighbor to destination
            return True
        
    return False  # Return False if no path is found

"""
Time Complexity Analysis:
- Exploring each edge in the graph: O(e), where e is the number of edges.
Overall: O(e)

Space Complexity Analysis:
- Recursive calls and call stack: O(n), where n is the number of nodes.
Overall: O(n)

Further Notes:
This algorithm utilizes a recursive Depth-First Search (DFS) approach to check for a path between two nodes in a graph. 
It starts from the source node and explores its neighbors recursively. If the destination node is reached during 
exploration, the function returns True, indicating that a path exists. Otherwise, if no path is found from any of 
the neighbors to the destination, the function returns False, indicating that there is no path between the 
source and destination nodes. The time complexity is O(e), where e is the number of edges in the graph, and 
the space complexity is O(n), where n is the number of nodes in the graph.
"""
