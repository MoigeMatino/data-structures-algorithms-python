def undirected_path(edges, node_A, node_B):
    """
    Determines if there exists a path between two nodes in an undirected graph.

    Args:
        edges (List[Tuple]): A list of tuples representing edges between nodes.
        node_A: The starting node.
        node_B: The destination node.

    Returns:
        bool: True if there is a path between node_A and node_B, False otherwise.

    """
    graph = build_graph(edges)  # Build the graph from the given edges
    return has_path(graph, node_A, node_B, set())  # Check if there is a path between node_A and node_B in the graph

def build_graph(edges):
    """
    Builds an undirected graph from a list of edges.

    Args:
        edges (List[Tuple]): A list of tuples representing edges between nodes.

    Returns:
        dict: A dictionary representing the undirected graph where keys are nodes and values are lists of neighboring nodes.

    """
    graph = {}  # Initialize an empty graph
    for edge in edges:
        a, b = edge
        # Add nodes and their neighbors to the graph
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)  # Add b as a neighbor of a
        graph[b].append(a)  # Add a as a neighbor of b
    return graph

def has_path(graph, src, dst, visited):
    """
    Checks if there is a path between two nodes in an undirected graph using Depth-First Search (DFS).

    Args:
        graph (dict): A dictionary representing the undirected graph where keys are nodes and values are lists of neighboring nodes.
        src: The source node.
        dst: The destination node.
        visited (set): A set of visited nodes.

    Returns:
        bool: True if there is a path from src to dst, False otherwise.

    """
    stack = [src]  # Initialize stack with the source node
    
    while stack:
        current = stack.pop()  # Pop a node from the stack
        
        if current == dst:  # If the current node is the destination, return True
            return True
        
        if current in visited:  # If the current node is already visited, continue to the next iteration
            continue
        
        visited.add(current)  # Mark the current node as visited
        
        for neighbor in graph[current]:  # Explore neighbors of the current node
            stack.append(neighbor)  # Add neighbors to the stack
    
    return False  # Return False if no path is found

"""
Time Complexity Analysis:
- Building the graph: O(e), where e is the number of edges.
- Exploring each edge in the graph: O(e), where e is the number of edges.
Overall: O(e)

Space Complexity Analysis:
- Storing nodes in the stack: O(n), where n is the number of nodes.
- Storing visited nodes: O(n), where n is the number of nodes.
Overall: O(n)

Further Notes:
This algorithm utilizes an iterative Depth-First Search (DFS) approach to check for a path between two nodes in an undirected graph. 
It starts from the source node and explores its neighbors iteratively using a stack data structure. If the destination node 
is encountered during exploration, the function returns True, indicating that a path exists. Otherwise, if no path is found 
from any of the neighbors to the destination, the function returns False, indicating that there is no path between the 
source and destination nodes. The time complexity is O(e), where e is the number of edges in the graph, and 
the space complexity is O(n), where n is the number of nodes in the graph.
"""
