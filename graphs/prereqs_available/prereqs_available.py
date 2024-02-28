from collections import defaultdict

# Function to check if completing prerequisites is possible without forming a cycle
def prereqs_possible(num_courses, prereqs):
    """
    Checks if completing prerequisites is possible without forming a cycle.

    Args:
        num_courses (int): The total number of courses.
        prereqs (List[Tuple[int, int]]): A list of tuples representing prerequisite relationships, 
                                          where each tuple contains the prerequisite course and the 
                                          course that depends on it.

    Returns:
        bool: True if completing prerequisites is possible without forming a cycle, False otherwise.
    """
    # Build the graph representing course prerequisites
    courses = build_graph(num_courses, prereqs)
    # Set to keep track of completed courses
    completed = set()
    # Set to keep track of courses in progress to detect cycles
    in_progress = set()
    
    # Start traversal from every single course
    for course in courses:
        # If cycle detected, return True
        if is_cycle(courses, course, completed, in_progress):
            return True
        
    # Return False if no cycle detected
    return False
    
# Function to build the graph of course prerequisites
def build_graph(num_courses, prereqs):
    """
    Builds the graph of course prerequisites.

    Args:
        num_courses (int): The total number of courses.
        prereqs (List[Tuple[int, int]]): A list of tuples representing prerequisite relationships, 
                                          where each tuple contains the prerequisite course and the 
                                          course that depends on it.

    Returns:
        defaultdict(list): A defaultdict where keys are courses and values are lists of courses 
                            that depend on the key course.
    """
    courses = defaultdict(list)
    for prereq_a, prereq_b in prereqs:
        courses[prereq_a].append(prereq_b)
        
    return courses
    
# Function to check for cycles using Depth-First Search (DFS)
def is_cycle(courses, course, completed, in_progress):
    """
    Checks for cycles using Depth-First Search (DFS).

    Args:
        courses (defaultdict(list)): A graph representing course prerequisites.
        course (int): The current course being explored.
        completed (set): A set of completed courses.
        in_progress (set): A set of courses in progress to detect cycles.

    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    # If course is already completed, no cycle can be formed
    if course in completed:
        return False
    # If course is in progress, it indicates a cycle
    if course in in_progress:
        return True
        
    in_progress.add(course)
    # Explore next courses recursively
    for next_course in courses[course]:
        if is_cycle(courses, next_course, completed, in_progress):
            return True
            
    # Remove course from in-progress set and add it to completed set
    in_progress.remove(course)
    completed.add(course)
    
    return False
"""
Time Complexity Analysis:
- Building the graph: O(p), where p is the number of prerequisites.
- Checking for cycles: O(n + p), where n is the number of courses and p is the number of prerequisites.
    - Each course is visited at most once, and each prerequisite relationship is traversed once.
Overall: O(n + p)

Space Complexity Analysis:
- Storing the graph: O(n), where n is the number of courses.
- Storing completed courses and courses in progress: O(n).
Overall: O(n)

FURTHER NOTES:
The aim is to assess whether it's possible to complete a set of course prerequisites without encountering 
circular dependencies, known as cycles. We achieve this by representing the prerequisites as a graph, where 
courses are nodes and prerequisite relationships are DIRECTED edges. The code utilizes depth-first search (DFS) 
to traverse the graph, checking for cycles as it explores each course. If a cycle is detected, indicating an 
unresolvable dependency loop, the function returns True, otherwise, it returns False, signifying that the 
prerequisites can be completed without circular dependencies. 
"""
