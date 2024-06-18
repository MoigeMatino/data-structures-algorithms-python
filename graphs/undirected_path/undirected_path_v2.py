def undirected_path(edges: list[tuple[int, int]], node_A: int, node_B: int) -> bool:
  """
  Checks if there exists a path between two nodes in an undirected graph.

  This function takes a list of edges `edges` representing an undirected graph, 
  two nodes `node_A` and `node_B`, and returns True if there exists a path
  between node_A and node_B in the graph, False otherwise. An undirected graph
  means connections between nodes go both ways (A to B is the same as B to A).

  Args:
      edges (list[tuple[int, int]]): A list of tuples representing edges in the graph.
          Each tuple contains two integers representing connected nodes.
      node_A (int): The starting node.
      node_B (int): The destination node.

  Returns:
      bool: True if a path exists between node_A and node_B, False otherwise.
  """

  graph = build_graph(edges)  # Build the graph dictionary from the edge list
  return has_path(graph, node_A, node_B, set())  # Start DFS traversal from node_A


def build_graph(edges: list[tuple[int, int]]) -> dict[int, list[int]]:
  """
  Builds an adjacency list representation of an undirected graph from a list of edges.

  This helper function takes a list of edges `edges` and constructs a dictionary 
  representation of the graph. The dictionary uses nodes as keys and stores lists of
  neighboring nodes (connected by edges) as values.

  Args:
      edges (list[tuple[int, int]]): A list of tuples representing edges in the graph.
          Each tuple contains two integers representing connected nodes.

  Returns:
      dict[int, list[int]]: A dictionary representing the adjacency list of the graph.
  """

  graph = {}  # Initialize an empty dictionary to store the graph

  for edge in edges:
    a, b = edge  # Unpack the edge tuple

    # Add nodes to the graph if they haven't been added yet
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []

    # Add undirected edges (both A to B and B to A)
    graph[a].append(b)
    graph[b].append(a)

  return graph


def has_path(graph: dict[int, list[int]], src: int, dst: int, visited: set[int]) -> bool:
  """
  Performs a depth-first search (DFS) traversal to find a path between two nodes.

  This helper function uses a recursive DFS approach to explore the graph starting
  from a source node `src` and searching for the destination node `dst`. It keeps track
  of visited nodes in the `visited` set to avoid cycles. The function recursively
  checks the neighbors of the current node and returns True if the destination node
  is found. Otherwise, it continues the exploration until all possibilities are
  exhausted, returning False if no path is found.

  Args:
      graph (dict[int, list[int]]): A dictionary representing the adjacency list of the graph.
      src (int): The source node for the DFS traversal.
      dst (int): The destination node to search for.
      visited (set[int]): A set to keep track of visited nodes during DFS exploration.

  Returns:
      bool: True if a path exists from src to dst, False otherwise.
  """

  if src == dst:  # Base case: If the source node is the destination, a path exists
    return True

  if src in visited:  # Avoid revisiting nodes (prevents infinite loops)
    return False

  visited.add(src)  # Mark the current node as visited

  # Explore each neighbor of the current node using DFS
  for neighbor in graph[src]:
    if has_path(graph, neighbor, dst, visited) == True:  # Check if a path exists from neighbor to dst
      return True  # If a path is found from a neighbor, return True

  return False  # If no path is found from any neighbor, return False

# Time Complexity: O(E)
# The time complexity of this algorithm is O(E), where E is the number of edges in the graph.

# Space: O(e)    
