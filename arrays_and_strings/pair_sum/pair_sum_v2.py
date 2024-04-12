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

# Example usage
numbers = [8, 7, 2, 1, 5]
target_sum = 10
result = pair_sum(numbers, target_sum)

if result:
  print(f"Pair found: ({numbers[result[0]]}, {numbers[result[1]]}) at indices ({result[0]}, {result[1]})")
else:
  print("No pair found that sums to", target_sum)

# Time Complexity: O(n^2)
# Time Complexity: O(n^2)
# The code uses nested loops to iterate through the list. In the worst case, the outer loop iterates n times,
# and for each iteration, the inner loop (using `diff in numbers`) iterates potentially n times.
# The code uses nested loops to iterate through the list. In the worst case, the outer loop iterates n times,
# and for each iteration, the inner loop (using `diff in numbers`) iterates potentially n times,
# resulting in a nested loop complexity of O(n * n) = O(n^2).

# Analogy: Imagine searching for a specific book in a bookshelf. The outer loop represents going through each shelf (each element in the list).
# The inner loop (implicit search) represents checking each book on the shelf (each element in the remaining list) to see if it's the one you're looking for.
# In the worst case, you might need to check every book on every shelf, resulting in quadratic time complexity.

# Space Complexity: O(1)
# The code uses constant additional space for temporary variables.

# Reasoning and Approach:
# This code implements a brute-force approach to find the pair that sums to the target sum.
# 1. **Nested Loops:** It uses nested loops to iterate through the `numbers` list.
#    - The outer loop iterates over each element (`num`) in the list.
#    - For each `num`, the inner loop (using `diff in numbers`) checks if the complement (`diff`) exists in the remaining elements of the list.
# 2. **Checking for Complement and Pair:** If the `diff` is found and it's not the same as the current `num`, it means a pair has been found. The function returns a tuple containing the indices of this pair.
# 3. **No Pair Found:** If the loops complete without finding a suitable complement, the function returns `None`.
