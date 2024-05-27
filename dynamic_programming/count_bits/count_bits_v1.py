def counting_bits(n: int) -> list[int]:
    """
    This function creates a lookup table containing the number of set bits (1s) for each non-negative integer
    from 0 to n (inclusive).

    Args:
        n (int): The upper limit for the non-negative integers (0 to n).

    Returns:
        list[int]: A list (lookup table) where the index represents the non-negative integer and the value
        at that index represents the number of set bits (1s) in its binary representation.
    """

    # Create a lookup table to store the number of set bits for each number
    lookup_table = [0] * (n + 1)  # Add 1 for size to accommodate numbers from 0 to n

    # Populate the lookup table using a bottom-up approach
    for num in range(n + 1):
        # Get the binary representation of the current number
        binary_repn = decimal_to_binary(num)

        # Count the number of 1s (set bits) in the binary representation
        num_of_ones = count_ones(binary_repn)

        # Store the count of 1s for the current number in the lookup table
        lookup_table[num] = num_of_ones

    return lookup_table


def decimal_to_binary(n: int) -> list[int]:
    """
    This function converts a non-negative integer to its binary representation as a list of digits.

    Args:
        n (int): The non-negative integer to convert to binary.

    Returns:
        list[int]: A list representing the binary digits (0s and 1s) of the input integer.
    """

    # Initialize an empty list to store the binary digits
    binary = []

    # Perform repeated division by 2 and store remainders (binary digits) until the number reaches 0
    while n > 0:
        quotient, remainder = divmod(n, 2)  # Get quotient and remainder from integer division by 2
        n = quotient  # Update n for the next iteration with the quotient (integer part)
        binary.append(remainder)  # Append the remainder (binary digit) to the list

    # Reverse the order of the binary digits to get the correct most-significant-bit (MSB) order
    return binary[::-1]


def count_ones(binary_repn: list[int]) -> int:
    """
    This function counts the number of occurrences of the value 1 (set bits) in a list representing a binary number.

    Args:
        binary_repn (list[int]): A list representing the binary digits (0s and 1s) of a number.

    Returns:
        int: The number of occurrences of the value 1 (set bits) in the input list.
    """

    # Use the built-in `count` method to efficiently count the number of 1s in the list
    return binary_repn.count(1)


# Time Complexity: O(n * log n)
#The time complexity of the `counting_bits` function is O(n log n). 
# The `decimal_to_binary` function has a time complexity of O(log n) for converting a decimal number to its binary representation.
# The `count_ones` function has a time complexity of O(log n) for counting the number of 1's in the binary representation.
# Additionally the `counting_bits` loops through the numbers with a time complexity of n.

# Space Complexity: O(n)
# The space complexity of this algorithm is O(n) due to the lookup table `lookup_table` that stores the 
# pre-computed results for n+1 numbers.

# Approach and Reasoning:
# 1. The algorithm iterates through each number from 0 to n and converts each number to its binary representation using the `decimal_to_binary` function.
# 2. The `count_ones` function counts the number of 1's in the binary representation of each number.
# 3. The results are stored in a lookup table, which is returned as the final result.
# 4. This approach leverages basic binary conversion and counting techniques to build the lookup table efficiently for the range of numbers from 0 to n.
