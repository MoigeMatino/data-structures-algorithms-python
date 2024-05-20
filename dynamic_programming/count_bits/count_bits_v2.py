def counting_bits(n: int) -> list[int]:
    """
    This function creates a lookup table containing the number of set bits (1s) for each non-negative integer
    from 0 to n (inclusive) using a dynamic programming approach.

    Args:
        n (int): The upper limit for the non-negative integers (0 to n).

    Returns:
        list[int]: A list (lookup table) where the index represents the non-negative integer and the value
        at that index represents the number of set bits (1s) in its binary representation.
    """

    # Create a lookup table to store the number of set bits for each number (0 to n)
    result = [0] * (n + 1)

    # Special case: For n = 0, the result is simply a list of 0s (no set bits)
    if n == 0:
        return result

    # Initialize the first two values in the table (0 and 1)
    result[0] = 0  # 0 has 0 set bits
    result[1] = 1  # 1 has 1 set bit

    # Iterate through the remaining numbers (2 to n)
    for x in range(2, n + 1):
        # Check if the current number is even
        if x % 2 == 0:
            # For even numbers, the number of set bits is the same as the number of set bits in half the number (x // 2)
            result[x] = result[x // 2]
        else:
            # For odd numbers, the number of set bits is one more than the number of set bits in half the number (x // 2)
            result[x] = result[x // 2] + 1

    return result


# Time Complexity: O(n)
# The time complexity of this algorithm is O(n). This is because the loop iterates through n+1 numbers 
# (from 0 to n) and for each number, a constant time operation is performed to calculate the number of set bits 
# based on the previously calculated value.

# Space Complexity: O(n)
# The space complexity of this algorithm is O(n) due to the lookup table `result` that stores the pre-computed 
# results for n+1 numbers.

# Approach and Reasoning:
# This algorithm uses a dynamic programming approach to efficiently calculate the number of set bits for all 
# non-negative integers from 0 to n. It leverages the observation that the number of set bits in the binary 
# representation of an even number is the same as the number of set bits in half the number (obtained by right-shifting 
# the binary representation by 1 bit). For odd numbers, the number of set bits is one more than the number of set bits 
# in half the number. This approach avoids redundant calculations by storing previously computed results in a lookup 
# table (`result`), leading to a more efficient solution compared to the v1 approach using separate functions 
# for decimal to binary conversion and counting ones.
