def pair_product(numbers: list[int], target_product: int) -> tuple[int, int]:
    """
    Finds a pair of numbers in a list that multiply to a given target product.

    Args:
        numbers (list[int]): A list of integers.
        target_product (int): The target product to find a pair for.

    Returns:
        tuple[int, int]: A tuple containing the indices of the two numbers
                         that multiply to the target product, or None if not found.
    """

    # Create an empty dictionary to store numbers and their corresponding indices
    number_indices: dict[int, int] = {}

    # Iterate through each number in the list
    for index, num in enumerate(numbers):
        # Calculate the quotient (target product divided by current number)
        quotient = target_product // num

        # Check if the quotient (potential pair) exists in the dictionary (meaning its pair has been seen)
        if quotient in number_indices:
            # If found, return the indices of the pair (quotient and current number)
            return number_indices[quotient], index

        # If not found, add the current number and its index to the dictionary for future lookups
        number_indices[num] = index

    # If no pair is found, return None
    return None

# Time Complexity: O(n)
# The code iterates through the list of numbers once in a loop, leading to linear time complexity.

# Space Complexity: O(n)
# The `number_indices` dictionary stores up to n unique numbers and their indices in the worst case.

# Approach and Reasoning:
# This algorithm leverages a hash table (implemented as a dictionary) for efficient pair lookups.
# 1. **Dictionary Initialization:** An empty dictionary `number_indices` is created to store numbers as keys and their corresponding indices in the list as values.
# 2. **Iterating through Numbers:** The code iterates through each number (`num`) in the `numbers` list using enumeration to get both the number and its index (`index`).
# 3. **Calculating Quotient:** It calculates the quotient by dividing the `target_product` by the current number (`num`). This quotient represents the potential pairing number we're looking for.
# 4. **Checking for Pair in Dictionary:** It checks if the `quotient` (potential pair) exists as a key in the `number_indices` dictionary.
#    - If the `quotient` is found:
#       - This means the current number (`num`) and the number at the index stored in `number_indices[quotient]` multiply to equal the `target_product`.
#       - The function immediately returns a tuple containing the indices of the matching pair (`number_indices[quotient]` and `index`).
#    - If the `quotient` is not found:
#       - It means no number has been seen yet that could pair with the current number (`num`) to reach the `target_product`.
#       - The current number (`num`) and its index (`index`) are added as a new key-value pair to the `number_indices` dictionary for future lookups.
# 5. **No Pair Found:** If the loop completes without finding a match, it means no pair exists in the list that multiplies to the `target_product`, and the function returns `None`.
