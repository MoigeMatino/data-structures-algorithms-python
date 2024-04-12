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

    # Create a dictionary to store seen numbers and their indices (Hash Table)
    previous_numbers = {}

    # Iterate through the numbers in the list
    for index, num in enumerate(numbers):
        # Calculate the complement (number needed to reach the target sum)
        complement = target_sum - num

        # Check if the complement has already been seen (exists in the dictionary)
        if complement in previous_numbers:
            # If found, return the indices of the pair (complement and current number)
            return (index, previous_numbers[complement])

        # If not seen yet, add the current number and its index to the dictionary
        previous_numbers[num] = index

    # If no pair is found, return None
    return None

# Time Complexity: O(n)
# The code iterates through the list of numbers once to create the hash table (O(n)).
# In the worst case, it iterates through the list again to find the complement (O(n)) for each number.
# However, on average, it's likely to find a pair much earlier, resulting in an average case closer to O(n).

# Space Complexity: O(n)
# The `previous_numbers` dictionary stores numbers and their indices, potentially holding all unique numbers from the list.
# In the worst case, this leads to a space complexity of O(n).
