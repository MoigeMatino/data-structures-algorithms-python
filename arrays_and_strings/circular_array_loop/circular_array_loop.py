def circular_array_loop(nums: list) -> bool:
    """
    Determines if the given array of integers forms a circular array loop.

    A circular array loop is defined as a sequence of indices in the array where:
    - You can start at any index and follow the steps defined by the values at each index.
    - The loop must be in a single direction (all positive or all negative).
    - The loop must contain more than one element.
    - The loop must return to the starting index.
    
    The function checks the following conditions:
    - The direction (forward or backward) of the current element must be the same as the direction of the previous element.
    - The step size must be greater than zero.
    If both of these conditions are met, the function continues to check the next element in the loop. If the loop completes without breaking, it means a circular array loop has been found and the function returns True. Otherwise, it returns False.

    Args:
        nums (list): The array of integers to check for a circular array loop.

    Returns:
        bool: True if the array contains a circular array loop, False otherwise.
    """
    size = len(nums)  # Get the length of the input array

    # Iterate over each index in the array
    for index in range(size):
        slow = fast = index  # Initialize two pointers, slow and fast, to the current index
        forward = nums[index] > 0  # Determine the direction of the current element

        while True:
            # Move the slow pointer to the next step
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                # If the slow pointer is not in a cycle, break the loop
                break

            # Move the fast pointer to the next step
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                # If the fast pointer is not in a cycle, break the loop
                break

            # Move the fast pointer to the next step again
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                # If the fast pointer is not in a cycle, break the loop
                break

            # If the slow and fast pointers meet, it means we have found a cycle
            if slow == fast:
                return True

    # If we have iterated over the entire array and not found a cycle, return False
    return False


def next_step(pointer, num_steps, size):
    """
    Calculate the next index in the array based on the current position and steps.

    This function handles wrapping around the array using modulo arithmetic.

    Args:
        pointer (int): The current index in the array.
        num_steps (int): The number of steps to move from the current index.
        size (int): The length of the array.

    Returns:
        int: The next index in the array.
    """
    result = (pointer + num_steps) % size
    if result < 0:
        result += size  # Adjust for negative indices to wrap around correctly
    return result


def is_not_cycle(nums, previous_direction, pointer):
    """
    Check if the current element does not form part of a valid cycle.

    A valid cycle must maintain the same direction and must not be a single-element loop.

    Args:
        nums (list): The array of integers.
        previous_direction (bool): The direction of the previous element (True for positive, False for negative).
        pointer (int): The current index in the array.

    Returns:
        bool: True if the current element does not form part of a valid cycle, False otherwise.
    """
    current_direction = nums[pointer] >= 0
    # Check if the direction has changed or if the step size is zero (invalid cycle)
    if (current_direction != previous_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    return False
