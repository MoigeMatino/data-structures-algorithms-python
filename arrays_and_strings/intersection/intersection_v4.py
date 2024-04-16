def intersection(a: list[int], b: list[int]) -> list[int]:
    """
    Finds the intersection of two sets of elements using sets for efficient lookups.

    Args:
        a (list[int]): The first list of elements.
        b (list[int]): The second list of elements.

    Returns:
        list[int]: A list containing the elements that are present in both lists.
    """

    # Convert list a to a set for efficient membership testing (O(1))
    return set(a).intersection(b)

# Time Complexity: O(n + m)
# - Converting list a to a set takes O(n) time in the worst case (all unique elements).
# - Finding the intersection using the `intersection` method of sets has an average time complexity
#   of O(k), where k is the number of elements in the intersection. In the worst case (no intersection),
#   it's still proportional to the size of the smaller set (dominant factor).

# Space Complexity: O(min(n, m))
# - The set operation creates a new set to store the intersection elements.
# - In the worst case, it will store all elements from the shorter list (min(n, m)).

# Approach and Reasoning:
# This approach leverages sets for efficient element lookups. By converting list `a` to a set,
# it enables constant time (O(1)) membership checks using the `intersection` method of sets.
# This significantly improves the efficiency compared to iterating through list `a` for each
# element in list `b`.

# Note:
# - This approach assumes you're dealing with hashable elements (e.g., integers, strings). 
# If you have non-hashable elements, you might need to consider alternative data structures or approaches.
