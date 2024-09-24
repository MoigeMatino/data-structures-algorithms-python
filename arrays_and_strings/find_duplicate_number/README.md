## **Problem Statement**

Given an array of positive numbers, `nums`, such that the values lie in the range `[1,n]`, inclusive, and that there are `n+1` numbers in the array, find and return the duplicate number present in `nums`. There is only one repeated number in `nums`.

**Note**: You cannot modify the given array nums. You have to solve the problem using only constant extra space.

Your task is to determine if `nums` has a cycle. Return TRUE if there is a cycle. Otherwise return FALSE.

### Constraints

> 1 ≤ n ≤ 10<sup>3</sup>

> nums.length = n+1

> 1 ≤ nums[i] ≤ n

All the integers in `nums` are unique, except for one integer that will appear more than once.


### Example 1
    Input: nums = [1, 3, 3, 4, 2, 5]
    Output: 3
    

### Example 2
    Input: nums = [1, 5, 3, 4, 2, 5]
    Output: 5

### Example 3
    Input: nums = [1, 2, 3, 4, 5, 6, 6, 7]
    Output: 6
    


