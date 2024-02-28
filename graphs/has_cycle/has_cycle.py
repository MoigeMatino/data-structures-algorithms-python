def has_cycle(graph):
    """
    Determines whether a directed graph has a cycle.

    Args:
        graph (dict): The directed graph represented as a dictionary where keys are nodes and 
                      values are lists of neighboring nodes.

    Returns:
        bool: True if the graph has a cycle, False otherwise.
    """
    visited = set()  # Set to store nodes that have been visited
    visiting = set() # Set to store nodes that are currently being visited
    for start_node in graph:  # Iterate through each node in the graph
        if cycle_detect(graph, start_node, visiting, visited):  # Check for cycles using cycle_detect function
            return True  # Return True if cycle is detected
    return False  # Return False if no cycle is detected

def cycle_detect(graph, node, visiting, visited):
    """
    Detects cycles in a directed graph using depth-first search (DFS).

    Args:
        graph (dict): The directed graph represented as a dictionary where keys are nodes and 
                      values are lists of neighboring nodes.
        node: The current node being explored.
        visiting (set): A set of nodes currently being visited in the DFS traversal.
        visited (set): A set of nodes already visited in the DFS traversal.

    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    if node in visited:  # If the current node has already been visited
        return False  # No cycle is detected

    if node in visiting:  # If the current node is being visited in the current traversal
        return True  # A cycle is detected

    visiting.add(node)  # Add the current node to the set of visiting nodes

    for neighbor in graph[node]:  # Iterate through neighboring nodes of the current node
        if cycle_detect(graph, neighbor, visiting, visited):  # Recursively check for cycles
            return True  # If a cycle is detected in the recursive call, return True

    visiting.remove(node)  # Remove the current node from the set of visiting nodes; cause it's been completely explored with no cycles found
    visited.add(node)  # Add the current node to the set of visited nodes
    return False  # No cycle is detected


"""
Time Complexity Analysis:
- Traversing the entire graph: O(e), where e is the number of edges.
Overall: O(e)

Space Complexity Analysis:
- Storing visited nodes: O(n), where n is the number of nodes.
- Storing nodes being visited(visiting): O(n).
Overall: O(n)

FURTHER NOTES:
The white-grey-black algorithm, is used to find cycles in directed acyclic graphs. 
The algorithm employs three sets: "white" set for unvisited nodes, "grey" set for nodes currently being explored 
in the DFS traversal, and "black" set for nodes that have been fully explored. By maintaining these sets, the algorithm 
detects cycles efficiently as it traverses the graph. This approach ensures that each node is visited exactly once and 
avoids revisiting nodes unnecessarily, leading to optimal time complexity. However, it requires additional space to store 
the sets, resulting in a space complexity proportional to the number of nodes in the graph.
"""
