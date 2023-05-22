def has_cycle(graph):
    visited = set()
    for start_node in graph:
        if cycle_detect(graph, start_node, set(), visited):
            return True
    return False

def cycle_detect(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False

"""
white-grey-black algorithm: used to find cycles in a DIRECTED graph

n = number of nodes
e = number of edges
Time: O(e)
Space: O(n)

"""