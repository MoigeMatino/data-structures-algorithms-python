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
    tracker_list = {}

    # Iterate through the numbers in the list
    for idx, num in enumerate(numbers):
        # Calculate the difference (complement) needed to reach the target sum (using walrus operator)
        diff = target_sum - num

        # Check if the complement (diff) has already been seen (exists in the dictionary)
        if diff in tracker_list:
            # If found, return the indices of the pair (complement and current number)
            return tracker_list[diff], idx

        # If not seen yet, add the current number and its index to the dictionary
        tracker_list[num] = idx

    # If no pair is found after iterating through the list, return None
    return None

# Time Complexity: O(n)
# The code iterates through the list of numbers once (O(n)) to create and update the hash table.
# In the worst case, it needs to check each number only once for its complement, resulting in a linear time complexity.

# Space Complexity: O(n)
# The `tracker_list` dictionary stores numbers and their indices, potentially holding all unique numbers from the list.
# In the worst case, this leads to a space complexity of O(n).

# Reasoning and Approach:
# This code utilizes a hash table (dictionary) for efficient pair finding.
# 1. **Hash Table Creation:** It iterates through the `numbers` list, adding each number and its corresponding index to the `tracker_list` dictionary.
#    - The walrus operator (`:=`) is used for concise assignment of `target_sum - num` to `diff` in the same line.
# 2. **Checking for Complement:** During each iteration, it calculates the `diff` (complement) needed to reach the `target_sum` with the current number.
# 3. **Pair Found or Not Seen:** It checks if the `diff` is already in the `tracker_list` (has been seen before).
#    - If `diff` is found, it means a pair has been found (the current number and the value from the `tracker_list` for the `diff`). The function immediately returns the indices of this pair.
#    - If `diff` is not seen yet, it adds `num` and its index to the `tracker_list`.
# 4. **No Pair Found:** If the loop completes without finding a suitable complement in the dictionary, it means no pair exists that sums to the `target_sum`. The function returns `None`.
