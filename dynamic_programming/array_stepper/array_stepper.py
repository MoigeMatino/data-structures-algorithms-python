def array_stepper(numbers: list[int]) -> bool:
    """
    Checks if it's possible to reach the end of a given array by jumping based on the values in the array.

    Args:
        numbers (list[int]): A list of integers, where each element represents the maximum number of steps
            you can jump from that position in the array.

    Returns:
        bool: True if it's possible to reach the last element of the array, False otherwise.

    This function implements a memoized recursive approach to determine if it's possible to reach the end
    of a given array by taking steps based on the values in the array. At each index, it explores all possible
    jumps (up to the maximum allowed steps) and checks if at least one jump leads to a reachable position
    (either the end of the array or a valid index from which further jumps can be made). Memoization is used
    to store previously computed results in a dictionary (`memo`) to avoid redundant calculations for
    subproblems (same index).
    """

    return _array_stepper(numbers, 0, {})  # Delegate the calculation to the helper function

def _array_stepper(numbers: list[int], i: int, memo: dict[int, bool]) -> bool:
    """
    Helper function for checking if a specific index in the array can reach the end.

    Args:
        numbers (list[int]): A list of integers, representing the maximum jump steps at each position.
        i (int): The current index in the array.
        memo (dict[int, bool]): A dictionary to store memoized results (index -> reachability).

    Returns:
        bool: True if it's possible to reach the end of the array from the current index, False otherwise.
    """

    # Check if the reachability from this index is already stored in the memo
    if i in memo:
        return memo[i]

    # Base case 1: Reached the end of the array (successful jump)
    if i >= len(numbers) - 1:
        return True  # Reachable

    # Base case 2: Invalid index (jumped out of bounds)
    if i < 0:
        return False  # Not reachable (jumped before the beginning)

    # Get the maximum number of steps allowed from the current index
    max_step = numbers[i]

    # Explore all possible jumps from the current index (up to the maximum allowed)
    for step in range(1, max_step + 1):
        # Check if a jump to this new index leads to a reachable position
        reachable = _array_stepper(numbers, i + step, memo)

        # If at least one jump leads to a reachable position, we can reach the end
        if reachable:
            memo[i] = True  # Store the result for future reference
            return True  # Reachable from this index

    # No successful jumps found from this index
    memo[i] = False  # Store the result for future reference
    return False  # Not reachable from this index

# Example usage
numbers = [2, 3, 1, 1, 4]
print(array_stepper(numbers))  # Output: True

# Time Complexity: O(n * max(numbers))
# - In the worst case, the function explores all possible jumps from each index (up to max_step).
# - This can lead to O(max(numbers)) for each index in the array.
# - As the number of indices (`n`) increases, the overall complexity becomes O(n * max(numbers)).

# Space Complexity: O(n)
# - The memoization dictionary can store the reachability for each unique index in the array.
# - In the worst case, it can hold entries for all `n` indices, resulting in O(n) space complexity.

# Approach and Reasoning:
# - This algorithm leverages memoization to avoid redundant calculations for subproblems (checking
#   reachability from the same index multiple times).
# - It utilizes a recursive approach to explore all possible jumps from each index and determine if at
#   least one jump leads to a reachable position (either the end of the array or a valid index for
#   further jumps).
# - By storing the reachability result for each index in the memo, the function avoids revisiting
#   the same subproblem and improves efficiency.
