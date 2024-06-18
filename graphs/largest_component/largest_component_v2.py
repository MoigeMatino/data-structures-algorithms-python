def largest_component(graph: dict[int, list[int]]) -> int:
  """
  Finds the size of the largest connected component in an undirected graph.

  This function takes an undirected graph represented as a dictionary `graph` as input. 
  The graph is a dictionary where keys are nodes (integers) and values are lists of neighbors
  (other nodes connected to the key node). The function uses an iterative depth-first search (DFS)
  approach to explore connected components and returns the size of the largest component
  (the largest group of nodes reachable from each other).

  Args:
      graph (dict[int, list[int]]): A dictionary representing the undirected graph. Keys are nodes,
                                    values are lists of neighboring nodes.

  Returns:
      int: The size of the largest connected component in the graph.
  """

  visited = set()  # Set to keep track of visited nodes during DFS exploration
  max_size = 0  # Variable to store the size of the largest component found so far

  # Iterate through each node in the graph (potential starting point for a DFS exploration)
  for node in graph:
    if node not in visited:  # Only explore unvisited nodes (avoid revisiting)
      size = explore_size(graph, node, visited)  # Explore the connected component starting from this node
      max_size = max(max_size, size)  # Update max size if the current component is larger

  return max_size


def explore_size(graph: dict[int, list[int]], node: int, visited: set[int]) -> int:
  """
  Explores a connected component in the graph using iterative DFS and returns its size.

  This helper function performs an iterative DFS traversal starting from a given node (`node`) 
  in the graph represented by the dictionary `graph`. It keeps track of visited nodes in the `visited` set.
  The function uses a stack to keep track of nodes to explore. It repeatedly pops a node from the stack,
  marks it as visited, and adds its unvisited neighbors to the stack. This process continues until the
  stack is empty, signifying the exploration of the entire connected component. The function returns
  the total number of nodes visited (size of the connected component).

  Args:
      graph (dict[int, list[int]]): A dictionary representing the undirected graph. Keys are nodes,
                                    values are lists of neighboring nodes.
      node (int): The starting node for the DFS exploration.
      visited (set[int]): A set to keep track of visited nodes during DFS exploration.

  Returns:
      int: The size (number of nodes) of the connected component explored from the starting node.
  """

  stack = [node]  # Stack to store nodes to be explored
  size = 0  # Initialize the size of the connected component

  while stack:
    current = stack.pop()  # Get the next node to explore from the stack
    if current in visited:  # Skip already visited nodes (avoid cycles)
      continue

    visited.add(current)  # Mark the current node as visited
    size += 1  # Increment the size of the connected component

    # Add unvisited neighbors of the current node to the stack for further exploration
    for neighbor in graph[current]:
      if neighbor not in visited:
        stack.append(neighbor)

  return size

# Time Complexity: O(E)
# The time complexity of this algorithm is O(E), where E is the number of edges in the graph. This is because
# the `explore_size` function performs an iterative DFS traversal. In the worst case, it might visit every edge
# in the graph once to explore all connected components. The outer loop in `largest_component` iterates through
# all nodes (V), but the dominant factor is the exploration within connected components.

# Space Complexity: O(n)
# The space complexity of this algorithm is O(V), where V is the number of nodes in the graph. This is because
# the `visited` set stores information about visited nodes, and in the worst case, it might need to store all
# nodes in the graph if they are part of a large connected component. Additionally, the stack used in the
# iterative DFS can grow up to V nodes deep in the worst case, depending on the structure of the graph.

# Note:
# This algorithm utilizes an iterative depth-first search (DFS) approach to explore connected components
