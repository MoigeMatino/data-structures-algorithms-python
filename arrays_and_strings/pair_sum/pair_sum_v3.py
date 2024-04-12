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

    # Create a dictionary (hash table) to store seen numbers and their indices
    tracker = {}

    # Iterate through the numbers in the list
    for index, num in enumerate(numbers):
        # Calculate the difference (complement) needed to reach the target sum
        diff = target_sum - num

        # Check if the current number (num) has not been seen before
        if num not in tracker:
            # If not seen, add the current number and its index to the tracker
            tracker[num] = index
        else:
            # If the complement (diff) exists in the tracker and its index is different from the current number's index:
            if diff in tracker and tracker[diff] != index:
                # A pair has been found! Return the indices of the pair (complement and current number)
                return tracker[diff], index

    # If no pair is found after iterating through the list, return None
    return None

# Time Complexity: O(n)
# The code iterates through the list of numbers once (O(n)) to create and update the hash table.
# In the worst case, it needs to check each number only once for its complement, resulting in a linear time complexity.

# Space Complexity: O(n)
# The `tracker` dictionary stores numbers and their indices, potentially holding all unique numbers from the list.
# In the worst case, this leads to a space complexity of O(n).

# Reasoning and Approach:
# This code utilizes a hash table (dictionary) for efficient pair finding.
# 1. **Hash Table Creation:** It iterates through the `numbers` list, adding each number and its corresponding index to the `tracker` dictionary.
# 2. **Checking for Complement:** During each iteration, it calculates the `diff` (complement) needed to reach the `target_sum` with the current number.
# 3. **Pair Found or Not Seen:** It checks if the `num` is already in the `tracker` (has been seen before).
#    - If `num` is not seen before, it adds `num` and its index to the `tracker`.
#   - If `num` is seen before, it checks if the `diff` (complement) exists in the `tracker` and its index is different from the current number's index.
#       - If the `diff` exists and their indices are different, it means a pair has been found (the current number and the value from the `tracker` for the `diff`). 
#        The function immediately returns the indices of this pair.
# 4. **No Pair Found:** If the loop completes without finding a suitable complement in the dictionary, it means no pair exists that sums to the `target_sum`. The function returns `None`.
