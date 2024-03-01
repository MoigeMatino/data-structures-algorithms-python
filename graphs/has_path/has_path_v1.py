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
    stack = [src]  # Initialize stack with the source node
    
    while stack:
        current = stack.pop()  # Pop a node from the stack
        
        if current == dst:  # If the current node is the destination, return True
            return True
        
        for neighbor in graph[current]:  # Explore neighbors of the current node
            stack.append(neighbor)  # Add neighbors to the stack
    
    return False  # Return False if no path is found

"""
Time Complexity Analysis:
- Exploring each edge in the graph: O(e), where e is the number of edges.
Overall: O(e)

Space Complexity Analysis:
- Storing nodes in the stack: O(n), where n is the number of nodes.
Overall: O(n)

Further Notes:
This algorithm utilizes an iterative Depth-First Search (DFS) approach to check for a path between two nodes in a graph. 
It starts from the source node and explores neighbors iteratively using a stack data structure. If the destination node 
is encountered during exploration, the function returns True, indicating that a path exists. Otherwise, if the stack 
becomes empty without encountering the destination node, the function returns False, indicating that there is no path 
between the source and destination nodes. The time complexity is O(e), where e is the number of edges in the graph, 
and the space complexity is O(n), where n is the number of nodes in the graph.
"""
