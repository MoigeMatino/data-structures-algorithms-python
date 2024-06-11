def intersection(a: list[int], b: list[int]) -> list[int]:
    """
    Finds the intersection of two sets of elements.

    Args:
        a (list[int]): The first list of elements.
        b (list[int]): The second list of elements.

    Returns:
        list[int]: A list containing the elements that are present in both lists.
    """

    # Create a set from list a for efficient membership testing (O(1))
    my_set = set(a)

    # Use list comprehension to filter elements from b that are in the set
    return [element for element in b if element in my_set]

# Time Complexity: O(n + m)
# - Converting list a to a set takes O(n) time in the worst case (all unique elements).
# - Filtering elements from list b using list comprehension takes up to O(m) time
#   (depending on how many elements are in the intersection).
# In total, the time complexity is linear in the sum of the lengths of the input lists (n + m).

# Space Complexity: O(min(n, m))
# - The `intersection` list stores the elements found in both lists.
# - In the worst case, it will store all elements from the shorter list (min(n, m)).

# Approach and Reasoning:
# This approach utilizes a set and list comprehension for efficient intersection.
# 1. **Set Conversion:** Converting list `a` to a set (`my_set`) allows for fast membership checks
#    using the `in` operator, which has a time complexity of O(1) in the average case.
# 2. **List Comprehension Filtration:** The list comprehension iterates through elements in `b`
#    and checks their membership in `my_set`. If an element is found in the set, it's included
#    in the resulting list. This approach is concise and avoids explicit loop construction.

# Note:
# - This approach assumes you're dealing with hashable elements (e.g., integers, strings).
# If you have non-hashable elements, you might need to consider alternative data structures or approaches.
