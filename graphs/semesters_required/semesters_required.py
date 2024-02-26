def semesters_required(num_courses, prereqs):
    # Build the graph representing course prerequisites
    graph = build_graph(prereqs, num_courses)
    # Dictionary to store the number of semesters required for each course
    no_of_semesters = {}
    # Initialize the no_of_semesters dict with the terminal courses
    for course in graph:
        if graph[course] == []:
            no_of_semesters[course] = 1
            
    # Start traversing the graph from each course
    for course in graph:
        get_semesters_required(course, graph, no_of_semesters)
    
    # Return the maximum semesters required among all courses
    return max(no_of_semesters.values())
    
def build_graph(prereqs, num_courses):
    # Build the directed acyclic graph
    graph = {course_id: [] for course_id in range(num_courses)}
    # graph = defaultdict(list)
    for course_a, course_b in prereqs:
        graph[course_a].append(course_b)
            
    return graph
    
def get_semesters_required(course, graph, no_of_semesters):
    # If semesters required for this course is already calculated, return it
    if course in no_of_semesters:
        return no_of_semesters[course]
        
    maximum = 0
    # Traverse through the prerequisite courses
    for neighbor_course in graph[course]:
        # Recursively calculate the semesters required for each prerequisite course
        temp_max = get_semesters_required(neighbor_course, graph, no_of_semesters)
        # Update the maximum semesters required among all prerequisites
        if temp_max > maximum:
            maximum = temp_max
            
    # Store the semesters required for the current course
    no_of_semesters[course] = 1 + maximum
    
    return no_of_semesters[course]


"""
p = # prereqs
c = # courses
Time: O(p)
Space: O(c)

FURTHER NOTES:
TO calculate the minimum number of semesters required to complete a given set of courses 
based on their prerequisites, we need to utilize a directed acyclic graph (DAG) representation 
where each course is a node and edges represent prerequisites. The graph built, represents the 
relationship between the nodes in the graph. Each key represents the prerequisite course and the 
values represent the courses that can be taken after the prerequisite.
By starting from the terminal courses (courses with no prerequisites;graph[course] == []), the 
algorithm guarantees that every course's semesters are calculated after its prerequisites, ensuring
an accurate count of the minimum semesters needed to complete each course. 
"""
