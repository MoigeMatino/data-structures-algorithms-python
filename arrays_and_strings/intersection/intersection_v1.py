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

    # Convert list a to a set for efficient membership testing (O(1))
    my_set = {element for element in a}

    # Iterate through elements in list b
    for element in b:
        # Check if the element is present in the set (converted from list a)
        if element in my_set:
            # If found, add it to the intersection list
            intersection.append(element)

    # Return the list containing the intersection elements
    return intersection

# Time Complexity: O(n + m)
# - Converting list a to a set takes O(n) time in the worst case (all unique elements).
# - Iterating through list b and checking for membership in the set takes O(m) time.
# In total, the time complexity is linear in the sum of the lengths of the input lists (n + m).

# Space Complexity: O(min(n, m))
# - The `intersection` list stores the elements found in both lists.
# - In the worst case, it will store all elements from the shorter list (min(n, m)).

# Approach and Reasoning:
# This algorithm leverages sets for efficient element lookups. By converting list a to a set, it enables 
# constant time (O(1)) membership checks using the `in` operator. This significantly improves the efficiency 
# compared to iterating through list a for each element in list b.

# Note:
# - This approach assumes you're dealing with hashable elements (e.g., integers, strings). If you have non-hashable elements, 
# you might need to consider alternative data structures or approaches.
