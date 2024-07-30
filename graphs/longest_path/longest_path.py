def longest_path(graph):
    """
    Calculate the longest path in a Directed Acyclic Graph (DAG) where the path length
    is defined as the number of edges from a node to a terminal node.

    Args:
        graph (dict): A dictionary representing the DAG where keys are node labels
                      and values are lists of adjacent nodes.

    Returns:
        int: The length of the longest path in the graph.
    """

    # Initialize a dictionary to keep track of distances of each node from a terminal node.
    distance = {}

    # Iterate through each node in the graph.
    for node in graph:
        # Check if the node is a terminal node (i.e., has no neighbors).
        if graph[node] == []:
            # Distance from a terminal node to itself is 0.
            distance[node] = 0

    # Start traversal of the graph from each node.
    for node in graph:
        # Call the helper function that mutates the distance dictionary.
        traverse_distance(graph, node, distance)

    # Finally, return the maximum value of the distances recorded.
    return max(distance.values())


def traverse_distance(graph, node, distance):
    """
    Helper function to recursively calculate the distance of each node from a terminal node.

    Args:
        graph (dict): The DAG represented as an adjacency list.
        node (any): The current node being processed.
        distance (dict): Dictionary storing the distances of nodes from terminal nodes.

    Returns:
        int: The distance of the current node from a terminal node.
    """

    # If the node's distance has already been calculated, return it.
    if node in distance:
        return distance[node]

    # Initialize the largest distance found among neighbors to 0.
    largest = 0

    # Iterate through each neighbor of the current node.
    for neighbor in graph[node]:
        # Recursively calculate the distance for the neighbor.
        temp = traverse_distance(graph, neighbor, distance)
        # Update the largest distance if the current neighbor's distance is greater.
        if temp > largest:
            largest = temp

    # Store the distance of the current node (1 + largest distance among neighbors).
    distance[node] = 1 + largest

    # Return the calculated distance for the current node.
    return distance[node]


"""
e = # edges
n = # nodes
Time: O(e)
Space: O(n)

NOTES:
The reasoning behind starting with the terminal nodes stems from the nature of directed acyclic graphs. 
In such graphs, there may exist numerous potential starting points for determining the longest path, without 
a clear indication of which one to choose. However, by identifying a terminal node, we establish a definitive
end point for all paths within the graph. Consequently, we can confidently trace back from this terminal node, 
considering each edge traversed as one unit of distance, thus facilitating the computation of the longest path 
from any other node, including the terminal node itself.

"""
        
