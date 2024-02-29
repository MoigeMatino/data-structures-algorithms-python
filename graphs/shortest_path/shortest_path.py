from collections import deque

def shortest_path(edges, node_A, node_B):
    """
    Finds the shortest path between two nodes in a graph.

    Args:
        edges (List[Tuple]): A list of tuples representing edges between nodes.
        node_A: The starting node.
        node_B: The target node.

    Returns:
        int: The shortest distance between node_A and node_B, or -1 if there's no path.

    """
    visited = set()  # Set to store visited nodes
    graph = make_graph(edges)  # Construct the graph
    queue = deque([ (node_A, 0) ])  # Initialize queue with the starting node and distance
    
    while queue:
        node, distance = queue.popleft()  # Dequeue a node and its distance
        
        if node == node_B:  # If the target node is reached, return the distance
            return distance
        
        for neighbor in graph[node]:  # Explore neighbors of the current node
            if neighbor not in visited:  # If neighbor is not visited, add it to visited set and enqueue it
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))  # Increment distance for the neighbor
    
    return -1  # Return -1 if no path is found    

def make_graph(edges):
    """
    Constructs a graph from a list of edges.

    Args:
        edges (List[Tuple]): A list of tuples representing edges between nodes.

    Returns:
        dict: A dictionary representing the graph where keys are nodes and values are lists of neighboring nodes.

    """
    graph = {}  # Initialize an empty graph
    for node1, node2 in edges:
        # Add nodes and their neighbors to the graph
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append(node2)  # Add node2 as a neighbor of node1
        graph[node2].append(node1)  # Add node1 as a neighbor of node2
    return graph

"""
Time Complexity Analysis:
- Constructing the graph: O(e), where e is the number of edges.
- Exploring nodes in the graph: O(e), where e is the number of edges.
Overall: O(e)

Space Complexity Analysis:
- Storing the graph: O(n), where n is the number of nodes.
- Storing visited nodes: O(n), where n is the number of nodes.
- Storing nodes in the queue: O(n), where n is the number of nodes.
Overall: O(n)

Further Notes:
The Breadth-First Search (BFS) approach is chosen for this algorithm because it explores all 
paths evenly, making it suitable for finding the shortest path between two nodes in a graph. 
A Depth-First Search (DFS) traversal might end up exploring a misleading direction until the 
very end of that path before exploring another node, even when the target node is closer to 
the source node through another path. By using BFS, we ensure that all possible paths are 
explored efficiently, leading to the discovery of the shortest path. The time complexity is 
O(e), where e is the number of edges, and the space complexity is O(n), where n is the number 
of nodes in the graph.
"""
