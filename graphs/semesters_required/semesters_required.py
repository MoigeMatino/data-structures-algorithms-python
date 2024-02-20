def semesters_required(num_courses, prereqs):
    graph = build_graph(prereqs, num_courses)
    no_of_semesters = {}
    # initiate the no_of_semesters dict with the terminal courses
    for course in graph:
        if graph[course] == []:
            no_of_semesters[course] = 1
            
    # start traversing the graph from each course
    for course in graph:
        get_semesters_required(course, graph, no_of_semesters)
    
    #return the semesters_required
    return max(no_of_semesters.values())
    
def build_graph(prereqs, num_courses):
    # build the directed acyclic graph
    graph = {course_id: [] for course_id in range(num_courses)}
    for course_a, course_b in prereqs:
        graph[course_a].append(course_b)
            
    return graph
    
def get_semesters_required(course, graph, no_of_semesters):
    if course in no_of_semesters:
        return no_of_semesters[course]
        
    maximum = 0
    for neighbor_course in graph[course]:
        temp_max = get_semesters_required(neighbor_course, graph, no_of_semesters)
        if temp_max > maximum:
            maximum = temp_max
            
    no_of_semesters[course] = 1 + maximum
    
    return no_of_semesters[course]

"""

p = # prereqs
c = # courses
Time: O(p)
Space: O(c)

"""
