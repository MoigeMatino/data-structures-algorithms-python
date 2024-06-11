def pair_sum(numbers, target_sum):
    """
    Finds a pair of numbers in the given list that sum to the target sum.

    Args:
        numbers (list): A list of integers.
        target_sum (int): The target sum to find.

    Returns:
        tuple: A tuple containing the indices of the two numbers that sum to the target sum, 
              or None if no such pair exists.
    """

    # Iterate through the numbers in the list (outer loop)
    for index, num in enumerate(numbers):
        # Calculate the difference (complement) needed to reach the target sum
        diff = target_sum - num

        # Check if the complement exists in the remaining list (inner loop)
        if diff in numbers and diff != num:
            # If found and not the current number itself, return the indices of the pair
            return index, numbers.index(diff)

    # If no pair is found, return None
    return None

# Time Complexity: O(n^2)
# The time complexity of the above algorithm is O(n^2), where n is the number of elements in the list `numbers`.
# This is because for each element in the list, we perform a membership test (using `in`), which in the worst case is O(n).

# Analogy: Imagine searching for a specific book in a bookshelf. The outer loop represents going through each shelf (each element in the list).
# The inner loop (implicit search) represents checking each book on the shelf (membership test) to see if it's the one you're looking for.
# In the worst case, you might need to check every book on every shelf, resulting in quadratic time complexity.

# Space Complexity: O(1)
# The space complexity of this algorithm is O(1) because it uses a constant amount of extra space (excluding
# temporary variables) regardless of the input size. It doesn't require any additional data structures that
# scale with the input size.

# Further Notes:
# 1. The approach uses a nested loop to find the pair of numbers that sum to the target. The outer loop iterates through each element, and the inner loop 
# checks if the complement (i.e., target_sum - num) exists in the list.
# 2. The check `diff != num` ensures that the same element is not used twice. 
# 3. This algorithm can be optimized using a dictionary to store the indices of the elements, which would reduce the time complexity to O(n).

# Optimized Approach:
# An optimized version of this algorithm can be achieved using a hash table (dictionary in Python) to store the indices of the elements. This reduces the overall time complexity to O(n).
