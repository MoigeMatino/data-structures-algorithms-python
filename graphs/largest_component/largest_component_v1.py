def largest_component(graph: dict[int, list[int]]) -> int:
  """
  Finds the size of the largest connected component in an undirected graph.

  This function takes an undirected graph represented as a dictionary `graph` as input. 
  The graph is a dictionary where keys are nodes (integers) and values are lists of neighbors
  (other nodes connected to the key node). The function explores the graph using depth-first
  search (DFS) and returns the size of the largest connected component (the largest group of nodes
  reachable from each other).

  Args:
      graph (dict[int, list[int]]): A dictionary representing the undirected graph. Keys are nodes,
                                    values are lists of neighboring nodes.

  Returns:
      int: The size of the largest connected component in the graph.
  """

  visited = set()  # Set to keep track of visited nodes during DFS exploration
  largest = 0  # Variable to store the size of the largest component found so far

  # Iterate through each node in the graph (potential starting point for a DFS exploration)
  for node in graph:
    size = explore_size(graph, node, visited)  # Explore the connected component starting from this node
    if size > largest:
      largest = size  # Update largest if the current connected component is bigger

  return largest


def explore_size(graph: dict[int, list[int]], node: int, visited: set[int]) -> int:
  """
  Explores a connected component in the graph using DFS and returns its size.

  This helper function performs a DFS traversal starting from a given node (`node`) in the graph 
  represented by the dictionary `graph`. It keeps track of visited nodes in the `visited` set. The function
  recursively explores unvisited neighbors of the current node and accumulates the total size (number of nodes)
  of the connected component reachable from the starting node.

  Args:
      graph (dict[int, list[int]]): A dictionary representing the undirected graph. Keys are nodes,
                                    values are lists of neighboring nodes.
      node (int): The starting node for the DFS exploration.
      visited (set[int]): A set to keep track of visited nodes during DFS exploration.

  Returns:
      int: The size (number of nodes) of the connected component explored from the starting node.
  """

  if node in visited:  # Check if the node has already been visited (avoid cycles)
    return 0

  visited.add(node)  # Mark the current node as visited

  size = 1  # Initialize the size of the connected component (including the starting node)

  # Recursively explore unvisited neighbors and add their sizes to the total size
  for neighbor in graph[node]:
    size += explore_size(graph, neighbor, visited)

  return size


# Time Complexity: O(E)
# The time complexity of this algorithm is O(E), where E is the number of edges in the graph. This is because
# the `explore_size` function performs a DFS traversal, and in the worst case, it might visit every edge
# in the graph once. The outer loop in `largest_component` iterates through all nodes (V), but the dominant
# factor is the exploration within connected components.

# Space Complexity: O(V)
# The space complexity of this algorithm is O(V), where V is the number of nodes in the graph. This is because
# the `visited` set stores information about visited nodes, and in the worst case, it might need to store all
# nodes in the graph if they are part of a large connected component.

# Note:
# This algorithm utilizes a depth-first search (DFS) approach to explore connected components in the graph.
# It iterates through each node in the graph and starts a DFS traversal from that node. The `explore_size`
# function recursively explores unvisited neighbors and keeps track of the total size of the connected
# component. The final result is the size of the largest connected component found during the exploration
# from all potential starting nodes.
