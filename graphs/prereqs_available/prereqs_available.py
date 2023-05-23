def prereqs_possible(num_courses, prereqs):
    graph = build_graph(num_courses, prereqs)
    visited = set()
    
    for node in range(0, num_courses):
        if has_cycle(graph, node, set(), visited):
            return False
        
    return True

def build_graph(num_courses, prereqs):
    graph = {}
    
    for id in range(num_courses):
        graph[id] = []
        
    for prereq in prereqs:
        course1_id, course2_id = prereq
        graph[course1_id].append(course2_id)
        
    return graph

def has_cycle(graph, node, visiting, visited):
    if node in visited:
        return False
    
    if node in visiting:
        return True
    
    visiting.add(node)
    
    for neighbor in graph[node]:
        if has_cycle(graph, neighbor, visiting, visited):
            return True
        
    visiting.remove(node)
    visited.add(node)
    
    return False