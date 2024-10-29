## **Problem Statement**

Given a sorted integer array, `nums`, and an integer value, `target`, the array is rotated by some arbitrary number. Search and return the index of `target` in this array. If the `target` does not exist, return `-1`.


### Constraints
- All values in nums are unique.
- The values in nums are sorted in ascending order.
- The array may have been rotated by some arbitrary number.
- 1 ≤ nums.length ≤1000≤1000
- −10<sup>4</sup> ≤ nums[i] ≤ 10<sup>4</sup>
- −10<sup>4</sup> ≤ target ≤ 10<sup>4</sup>

## **Examples**

### Example 1: Target Found in Rotated Array

**Input:**

- `nums = [4, 5, 6, 7, 0, 1, 2]`
- `target = 0`

**Process:**
- The array `[4, 5, 6, 7, 0, 1, 2]` is a sorted array that has been rotated.
- The target value `0` is located at index `4`.

**Output:** `4`

**Visualization:**
- Original Sorted Array: [0, 1, 2, 4, 5, 6, 7]
- Rotated Array:         [4, 5, 6, 7, 0, 1, 2]
- Target: 0
- Index of Target: 4

### Example 2: Target Not Found

**Input:**
- `nums = [4, 5, 6, 7, 0, 1, 2]`
- `target = 3`

**Process:**
- The array `[4, 5, 6, 7, 0, 1, 2]` is a sorted array that has been rotated.
- The target value `3` is not present in the array.

**Output:** `-1`

**Visualization:**

Original Sorted Array: [0, 1, 2, 4, 5, 6, 7]
Rotated Array:         [4, 5, 6, 7, 0, 1, 2]
Target:                3
Index of Target:       -1 (not found)


### Example 3: Target Found at Beginning

**Input:**
- `nums = [6, 7, 0, 1, 2, 4, 5]`
- `target = 6`

**Process:**
- The array `[6, 7, 0, 1, 2, 4, 5]` is a sorted array that has been rotated.
- The target value `6` is located at index `0`.

**Output:** `0`

**Visualization:**

- Original Sorted Array: [0, 1, 2, 4, 5, 6, 7]
- Rotated Array:         [6, 7, 0, 1, 2, 4, 5]
- Target:                6
- Index of Target:       0


### Example 4: Target Found at End

**Input:**
- `nums = [6, 7, 0, 1, 2, 4, 5]`
- `target = 5`

**Process:**
- The array `[6, 7, 0, 1, 2, 4, 5]` is a sorted array that has been rotated.
- The target value `5` is located at index `6`.

**Output:** `6`

**Visualization:**

- Original Sorted Array: [0, 1, 2, 4, 5, 6, 7]
- Rotated Array:         [6, 7, 0, 1, 2, 4, 5]
- Target:                5
- Index of Target:       6