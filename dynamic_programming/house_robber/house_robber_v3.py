def house_robber_circular(money: list[int]) -> int:
    """
    This function calculates the maximum amount of money a robber can steal without robbing adjacent houses
    in a circular street of houses.

    Args:
        money (list[int]): A list representing the amount of money in each house on the circular street.

    Returns:
        int: The maximum amount of money the robber can steal.
    """

    # Handle empty or single-house cases (edge cases)
    if len(money) == 0:
        return 0
    elif len(money) == 1:
        return money[0]

    # Two approaches are possible to solve the house robber problem on a circular street:
    # 1. Using memoization with explicit starting and ending indices (previous approach)
    # 2. Using dynamic programming with a table (current approach)

    # This approach uses a table to store the maximum amount achievable at each house in the street.

    # Calculate the maximum amount considering excluding the first house (treated as a non-circular street)
    wout_first_house = _house_robber(money[1:])

    # Calculate the maximum amount considering excluding the last house (treated as a non-circular street)
    wout_last_house = _house_robber(money[:-1])

    # The robber cannot steal from both the first and last house in a circular street.
    # Return the maximum between excluding the first house and excluding the last house.
    return max(wout_first_house, wout_last_house)


def _house_robber(money: list[int]) -> int:
    """
    This helper function uses dynamic programming with a table to calculate the maximum amount of money
    a robber can steal without robbing adjacent houses, considering a non-circular street (all houses).

    Args:
        money (list[int]): A list representing the amount of money in each house on the street.

    Returns:
        int: The maximum amount of money the robber can steal considering the entire street.
    """

    # Create a table to store the maximum amount achievable at each house (0-based indexing)
    table = [0 for i in range(len(money) + 1)]

    # Base cases:
    # table[0] = 0 (no house, no money)
    table[0] = 0

    # table[1] = money[0] (maximum achievable with only the first house)
    table[1] = money[0]

    # Fill the table iteratively for houses starting from the second one (index 2)
    for i in range(2, len(money) + 1):
        # Why money[i - 1] here:
        # - We are calculating the maximum amount achievable at house i (index i-1).
        # - To decide the maximum, we consider two options:
        #   1. Including the current house (i): We add the money from this house (money[i-1])
        #      to the maximum achievable amount from the house two houses before (i-2) (table[i-2]).
        #   2. Excluding the current house (i): We simply take the maximum achievable amount
        #      from the previous house (i-1) (table[i-1]).

        including_current_amount = money[i - 1] + table[i - 2]
        excluding_current_amount = table[i - 1]

        # Store the maximum achievable amount at the current house (i) in the table
        table[i] = max(including_current_amount, excluding_current_amount)

    # Return the maximum amount achievable from the last house (end of the table)
    return table[-1]
    
# Time and Space Complexities

# - Time Complexity: O(n)
#   The time complexity is linear because each house is processed a constant number of times. The main function calls 
#   the helper function twice, and the helper function processes each house in a loop.

# - Space Complexity: O(n)
#   The space complexity is linear due to the table used in the helper function to store the maximum money that can be robbed up to each house.

# Further Notes

# - Tabulation(bottom-up) Approach: This solution uses tabulation to solve the problem. The helper function builds a table where each entry 
#   represents the maximum money that can be robbed up to that house, considering the constraint of not robbing two adjacent houses.
# - Circular Nature Handling: The problem of circular houses is handled by solving two separate subproblems:
#   1. Excluding the first house (i.e., considering houses from index 1 to the end).
#   2. Excluding the last house (i.e., considering houses from index 0 to the second last house).
#   This ensures that no two adjacent houses in the circle are robbed.
# - Slicing Lists: While slicing creates new lists, it simplifies the problem of handling the circular nature of the houses. 
#    In a more optimized version, indices could be used to avoid the overhead of list slicing.
# - Edge Cases: The code handles edge cases such as empty lists and lists with only one house. For an empty list, it returns 0, and for a single 
#    house, it returns the value of that house.
