from typing import List, bool


def find_sum_of_three(nums: List[int], target: int) -> bool:
  """
  Finds if there exists a triplet in the given list that sums to the target sum.

  This function takes a list of integers `nums` and an integer `target` as input. It returns True if there
  exist three elements in the list that add up to the target sum, and False otherwise.

  Args:
      nums (List[int]): A list of integers.
      target (int): The target sum to find.

  Returns:
      bool: True if there exists a triplet in the list that sums to the target sum, False otherwise.
  """

  # Sort the input list to efficiently find combinations using two pointers (low and high)
  nums.sort()

  # Iterate through the list up to the second-last element (avoiding out-of-bounds access)
  for i in range(len(nums) - 2):
    # Skip duplicates of the current element (i) to potentially avoid redundant checks (optimization)
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    low = i + 1  # Initialize the low pointer to the element after the current element (i)
    high = len(nums) - 1  # Initialize the high pointer to the last element

    # Two-pointer approach to find triplets that sum to the target
    while low < high:
      current_sum = nums[i] + nums[low] + nums[high]  # Calculate the current sum of the triplet

      # If the sum is equal to the target, return True (triplet found)
      if current_sum == target:
        return True

      # If the sum is less than the target, move the low pointer forward to increase the sum
      elif current_sum < target:
        low += 1

      # If the sum is greater than the target, move the high pointer backward to decrease the sum
      else:
        high -= 1

  # If no triplet is found after iterating through all possible combinations, return False
  return False

# Time Complexity: O(n^2)
# The time complexity of this algorithm is O(n^2) due to the nested loop structure. The outer loop iterates
# through the list (n elements), and the inner loop (two-pointer approach) iterates at most n times in the worst
# case for each element in the outer loop. However, due to early termination within the inner loop when duplicates
# are skipped (optimization), the average time complexity might be slightly better than O(n^2) in practice.

# Space Complexity: O(1)
# The space complexity of this algorithm is O(1) because it uses a constant amount of extra space (excluding
# temporary variables) regardless of the input size. It modifies the input list in-place for sorting, but this doesn't
# affect the asymptotic space complexity.

# Note:
# This algorithm utilizes a similar two-pointer approach as the `three_sum` function, but it's modified to find
# if any triplet sums to the target instead of requiring all triplets to be unique. The early termination for
# duplicate elements (optimization) can potentially reduce redundant checks in the inner loop. It's important to note
# that the function returns True as soon as a qualifying triplet is found and doesn't enumerate all possible triplets.
