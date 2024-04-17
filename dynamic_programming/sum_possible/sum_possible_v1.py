def sum_possible(amount: int, numbers: list[int]) -> bool:
    """
    Checks if a given target amount can be formed using any combination of numbers from a list.

    Args:
        amount (int): The target amount to achieve.
        numbers (list[int]): A list of integers representing the available numbers.

    Returns:
        bool: True if the target amount can be formed using the numbers, False otherwise.

    This function implements a brute-force recursive approach to determine if the target amount ('amount')
    can be formed using any combination of numbers from the provided list ('numbers').

    **Brute Force Approach:**
    The function iterates through each number ('num') in the list. For each number, it recursively
    calls itself with the remaining amount ('amount - num') and the same list of numbers ('numbers').
    This effectively explores all possible combinations of numbers that could sum up to the target amount.

    - If any of these recursive calls return True (meaning a combination was found), the function
      immediately returns True, indicating that a solution exists.

    - If the loop completes without finding a successful combination (all recursive calls return False),
      the function returns False, indicating that no combination exists to reach the target amount.

    """

    # Base case: If the target amount is 0, a valid combination is found (empty sum)
    if amount == 0:
        return True

    # Base case: If the target amount is negative, no valid combination exists
    if amount < 0:
        return False

    # Try each number in the list
    for num in numbers:
        # Check if the remaining amount can be formed using the remaining numbers
        if sum_possible(amount - num, numbers):
            # If a combination is found, return True (early termination)
            return True

    # If none of the numbers led to a solution, return False
    return False

# Time Complexity: O(n^a)
# - In the worst case, the function explores all possible combinations of numbers.
# - For each number 'num', a recursive call is made, potentially leading to further recursive calls.
# - The number of recursive calls can grow exponentially with the target amount 'a' and the number of choices 'n'
#   (number of elements in 'numbers'). This results in a time complexity of O(n^a).

# Space Complexity: O(n)
# - The space complexity is primarily due to the recursive call stack.
# - In the worst case, the call stack depth can be up to 'n' (number of elements in 'numbers') for a particular
#   combination attempt. This results in a space complexity of O(n).

# Approach and Reasoning:
# This approach utilizes a simple brute-force recursive strategy. It explores all possible combinations
# of numbers in the list to see if any combination adds up to the target amount.
