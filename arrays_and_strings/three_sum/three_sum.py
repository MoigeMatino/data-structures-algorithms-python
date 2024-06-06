from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
  """
  Finds all unique triplets in the given list that sum to zero.

  This function takes a list of integers `nums` as input and returns a list of all unique triplets
  where each triplet consists of three elements from the input list that add up to zero.

  Args:
      nums (List[int]): A list of integers.

  Returns:
      List[List[int]]: All unique triplets in the given list that sum to zero.
  """

  # Sort the input list to efficiently find combinations using two pointers (low and high)
  nums.sort()
  triplets = []  # Initialize an empty list to store the found triplets

  # Iterate through the list up to the second-last element (avoiding out-of-bounds access)
  for i in range(len(nums) - 2):
    # Skip duplicates of the current element (i) to avoid redundant triplets
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    low = i + 1  # Initialize the low pointer to the element after the current element (i)
    high = len(nums) - 1  # Initialize the high pointer to the last element

    # Two-pointer approach to find triplets that sum to zero
    while low < high:
      current_sum = nums[i] + nums[low] + nums[high]  # Calculate the current sum of the triplet

      # If the sum is zero, append the triplet to the result and skip duplicates
      if current_sum == 0:
        triplets.append([nums[i], nums[low], nums[high]])
        # Skip duplicates of the low pointer to avoid redundant triplets
        while low < high and nums[low] == nums[low + 1]:
          low += 1
        # Skip duplicates of the high pointer to avoid redundant triplets
        while low < high and nums[high] == nums[high - 1]:
          high -= 1
        low += 1  # Move the low pointer forward for the next iteration
        high -= 1  # Move the high pointer backward for the next iteration

      # If the sum is less than zero, move the low pointer forward to increase the sum
      elif current_sum < 0:
        low += 1

      # If the sum is greater than zero, move the high pointer backward to decrease the sum
      else:
        high -= 1

  return triplets


# Time Complexity: O(n^2)
# The time complexity of this algorithm is O(n^2) due to the nested loop structure. The outer loop iterates
# through the list (n elements), and the inner loop (two-pointer approach) iterates at most n times in the worst
# case for each element in the outer loop. However, due to early termination within the inner loop when duplicates
# are skipped, the average time complexity might be slightly better than O(n^2) in practice.

# Space Complexity: O(1)
# The space complexity of this algorithm is O(1) because it uses a constant amount of extra space (excluding
# the output list) regardless of the input size. It modifies the input list in-place for sorting, but this doesn't
# affect the asymptotic space complexity.

# Note:
# This algorithm utilizes a two-pointer approach to efficiently find triplets that sum to zero. By sorting the input
# list first, we can use pointers to iterate through the list and combine elements while ensuring they are in the
# correct order for the sum to be zero. The additional checks for duplicate elements within the inner loop help to
# avoid generating redundant triplets in the result list.
