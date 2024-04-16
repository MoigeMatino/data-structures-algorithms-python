def intersection(a: list[int], b: list[int]) -> list[int]:
    """
    Finds the intersection of two sets of elements.

    Args:
        a (list[int]): The first list of elements.
        b (list[int]): The second list of elements.

    Returns:
        list[int]: A list containing the elements that are present in both lists.
    """

    # Create an empty list to store the intersection elements
    intersection = []

    # Iterate through elements in list b
    for element in b:
        # Check if the element is present in list a (potentially inefficient)
        if element in a:
            # If found, add it to the intersection list
            intersection.append(element)

    # Return the list containing the intersection elements
    return intersection

# Time Complexity: O(n * m)
# - In the worst case, the nested loop iterates through all elements in list b (length m)
#   and checks for membership in list a (length n) for each element.
# - This can result in a total of n * m comparisons.

# Space Complexity: O(min(n, m))
# - The `intersection` list stores the elements found in both lists.
# - In the worst case, it will store all elements from the shorter list (min(n, m)).

# Approach and Reasoning:
# This approach iterates through each element in list `b` and checks if it exists in list `a` using a linear search. 
# However, this can be inefficient for larger lists due to the nested loop structure leading to O(n * m) time complexity.

# Note:
# - This is a basic implementation for finding intersections. It's generally less efficient
#   than using sets, which offer constant time lookups (O(1)) for membership checks.
# - Consider using the alternative approach with sets for better performance, especially
#   when dealing with larger datasets.
