
# Dummy API call to check if a version is bad
def is_bad_version(s):
    v = 5
    return s >= v  # Assume v is a variable representing the first bad version

def first_bad_version(n):
    """
    Finds the first bad version in a sequence of versions using a binary search approach.

    This function uses a binary search algorithm to efficiently determine the first bad version
    in a sequence of versions from 1 to n. It minimizes the number of API calls to the is_bad_version
    function by halving the search space at each step.

    Args:
        n: The total number of versions.

    Returns:
        A tuple containing the first bad version and the number of API calls made.
    """
    first = 1  # Initialize the first pointer to the start of the version sequence
    last = n   # Initialize the last pointer to the end of the version sequence
    api_calls = 0  # Counter to track the number of API calls made

    # Perform binary search to find the first bad version
    while first <= last:
        mid = first + (last - first) // 2  # Calculate the middle point to avoid overflow
        if is_bad_version(mid):  # make api call to check if the middle version is bad
            last = mid - 1  # If it is, search the left half
        else:
            first = mid + 1  # If it is not, search the right half
        
        api_calls += 1  # Increment the API call counter

    return first, api_calls  # Return the first bad version and the number of API calls

# Time Complexity: O(log n)
# The algorithm runs in logarithmic time because it uses a binary search approach, which divides the search space in half at each step.

# Space Complexity: O(1)
# The algorithm uses a constant amount of extra space. It only uses a few integer variables and does not require any additional data structures that depend on the size of the input.

# Approach:
# 1. Use a binary search to efficiently find the first bad version in a sequence of versions.
# 2. Initialize two pointers, first and last, to represent the search range.
# 3. Calculate the middle version and use the is_bad_version API to check if it is bad.
# 4. Adjust the search range based on whether the middle version is bad or not.
# 5. Continue the search until the first pointer surpasses the last pointer.
# 6. Return the first bad version and the number of API calls made.
# This approach minimizes the number of API calls by leveraging the binary search technique.