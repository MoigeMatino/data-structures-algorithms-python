def find_duplicate_number(nums: list[int]):
    # Initialize two pointers, both starting at the first element of the array.
    # These pointers will be used to detect a cycle in the array.
    fast = slow = nums[0]
    
    # Phase 1: Detect the cycle using Floyd's Tortoise and Hare algorithm.
    while True:
        # Move the slow pointer one step at a time.
        slow = nums[slow]
        # Move the fast pointer two steps at a time.
        fast = nums[nums[fast]]
        
        # If the slow and fast pointers meet, a cycle is detected.
        if slow == fast:
            break
    
    # Phase 2: Find the entry point of the cycle, which is the duplicate number.
    # Reset the slow pointer to the start of the array.
    slow = nums[0]
    
    # Move both pointers one step at a time until they meet.
    # The meeting point is the entry point of the cycle, which is the duplicate number.
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    # Return the duplicate number.
    return fast

# Time Complexity: O(n)
# The algorithm runs in linear time because both the cycle detection and the cycle entry point
# finding phases require at most n steps each, where n is the number of elements in the array.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. It only uses a few integer variables
# (slow, fast) and does not require any additional data structures that depend on the size of the input array.

# Rationale:
# The approach uses Floyd's Tortoise and Hare algorithm, which is typically used for cycle detection in linked lists.
# Here, the array is treated as a linked list where each index points to the next index.
# The duplicate number creates a cycle because it points back to an earlier index in the list.
# This method efficiently finds the duplicate without modifying the input array or using extra space.