def semesters_required(num_courses, prereqs):
    distance = {}
    
    graph = build_graph(num_courses, prereqs)
    
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 1
        
    for node in graph:    
        traversal_distance(graph, node, distance)
        
    return max(distance.values())
    
def build_graph(prereqs, num_courses):
    graph = {course_id: [] for course_id in range(num_courses)}
    for course_a, course_b in prereqs:
        if course_b not in graph[course_a]:
            graph[course_a].append(course_b)            
            
    return graph

def traversal_distance(graph, node, distance):
    if node in distance:
        return distance[node]
    
    max = 0
    
    for neighbor in graph[node]:
        temp = traversal_distance(graph, neighbor, distance)
        if temp > max:
            max = temp
    
    distance[node] = 1 + max
    
    return distance[node]

"""

p = # prereqs
c = # courses
Time: O(p)
Space: O(c)

"""
