def longest_path(graph):
    # initialise a dictionary to keep track of distances of each node from a terminal node
    distance = {}
    
    for node in graph:
        if graph[node] == []:# this indicates a terminal node due to absence of neighbors
            distance[node] = 0 # distance from a terminal node to a terminal node is 0

    # start traversal of graph from each node
    for node in graph:
        # pass to helper function that mutates the distance dictionary
        traverse_distance(graph, node, distance)

    # finally return the max value of the distance dictionary values 
    return max(distance.values())

def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node] # return the distance of the node from the terminal node if already precalculated
    
    largest = 0

    for neighbor in graph[node]:
        temp = traverse_distance(graph, neighbor, distance) # note here that the recursive call returns a number ie. distance from neighbor to terminal node
        if temp > largest:
            largest = temp
    
    distance[node] = 1+largest # store the distance of the current node from terminal node so that it does not have to be recalculated 
    
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
        
