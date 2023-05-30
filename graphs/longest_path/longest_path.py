def longest_path(graph):
    distance = {}
    
    for node in graph:
        if graph[node] == []:# this indicates a terminal node due to absence of neighbors
            distance[node] = 0
        
    for node in graph:
        traverse_distance(graph, node, distance)
        
    return max(distance.values())

def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]
    
    largest = 0

    for neighbor in graph[node]:
        temp = traverse_distance(graph, neighbor, distance)
        if temp > largest:
            largest = temp
    
    distance[node] = 1+largest    
    
    return distance[node]

"""

e = # edges
n = # nodes
Time: O(e)
Space: O(n)

"""
        
