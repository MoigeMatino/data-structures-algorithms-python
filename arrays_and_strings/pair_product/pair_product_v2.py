def pair_product_v2(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Finds a pair of numbers in a sorted list that multiply to a given target product.

    Args:
        nums (list[int]): A sorted list of integers.
        target (int): The target product to find a pair for.

    Returns:
        tuple[int, int]: A tuple containing the indices of the two numbers
                         that multiply to the target product, or None if not found.
    """

    # Create a dictionary to store numbers and their corresponding indices (faster lookup)
    num_indices = {num: index for index, num in enumerate(nums)}

    # Initialize pointers for two-pointer search (i at beginning, j at end)
    i = 0
    j = len(nums) - 1

    # Loop while the pointers haven't crossed
    while i < j:
        # Calculate the current product of elements pointed to by i and j
        current_product = nums[i] * nums[j]

        # Check if the current product matches the target
        if current_product == target:
            # Found a pair, return their indices from the dictionary
            return num_indices[nums[i]], num_indices[nums[j]]

        # If the current product is less than the target, move the left pointer (i) forward
        elif current_problem < target:
            i += 1

        # If the current product is greater than the target, move the right pointer (j) backward
        else:
            j -= 1

    # If the loop completes without finding a pair, return None
    return None

# Time Complexity: O(n log n)
# The loop iterates through the list only once, resulting in O(n) time complexity. 
# However, since sorting is the dominant factor, the overall time complexity is considered O(n log n).

# Space Complexity: O(n)
# The `num_indices` dictionary stores up to n unique numbers and their indices in the worst case.

# Approach and Reasoning:
# This algorithm uses two key techniques:
# 1. **Sorting:** It requires the input list `nums` to be sorted in ascending order beforehand.
#    - Sorting allows for efficient two-pointer search because we can guarantee that
#      elements to the left of `i` are less than or equal to `nums[i]` and elements to the
#      right of `j` are greater than or equal to `nums[j]`.
# 2. **Two-Pointer Search:** It utilizes two pointers, `i` and `j`, initially positioned
#    at the opposite ends of the sorted list. The pointers are then moved inwards based
#    on the comparison between the `current_product` and the `target`:
#    - If `current_product` is less than `target`, it means the pair's product needs to
#      be bigger. So, we move the left pointer (`i`) forward to consider larger elements.
#    - If `current_product` is greater than `target`, it means the pair's product needs to
#      be smaller. So, we move the right pointer (`j`) backward to consider smaller elements.
#    - If `current_product` matches `target`, we found the pair and return their indices.
