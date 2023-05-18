def semesters_required(num_courses, prereqs):
    distance = {}
    
    graph = build_graph(num_courses, prereqs)
    
    for node in graph:
        if len(graph[node]) == 0:
            distance[node] = 1
        
    for node in graph:    
        traversal_distance(graph, node, distance)
        
    return max(distance.values())
    
def build_graph(num_courses, prereqs):
    graph = {}
    
    for course_id in range(num_courses):
        graph[course_id] = []
    
    for prereq in prereqs:
        course_a_id, course_b_id = prereq
            
        graph[course_a_id].append(course_b_id)
        
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