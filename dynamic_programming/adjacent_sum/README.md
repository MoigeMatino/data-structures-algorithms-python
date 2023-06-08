# non adjacent sum

Write a function, `non_adjacent_sum`, that takes in a list of numbers as an argument. The function should return the maximum sum of non-adjacent items in the list. There is no limit on how many items can be taken into the sum as long as they are not adjacent.

For example, given:

[2, 4, 5, 12, 7]

The maximum non-adjacent sum is 16, because 4 + 12. 
4 and 12 are not adjacent in the list.

## test_0

```python
nums = [2, 4, 5, 12, 7]
non_adjacent_sum(nums) # -> 16
```

## test_0

```python
nums = [7, 5, 5, 12]
non_adjacent_sum(nums) # -> 19
```

## test_0

```python
nums = [7, 5, 5, 12, 17, 29]
non_adjacent_sum(nums) # -> 48
```

## test_0

```python
nums = [
  72, 62, 10,  6, 20, 19, 42,
  46, 24, 78, 30, 41, 75, 38,
  23, 28, 66, 55, 12, 17, 9,
  12, 3, 1, 19, 30, 50, 20
]
non_adjacent_sum(nums) # -> 488
```

## test_0

```python
nums = [
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  83, 80, 56, 68,  6, 22, 56, 96, 77, 98,
  61, 20,  0, 76, 53, 74,  8, 22, 92, 37,
  30, 41, 75, 38, 23, 28, 66, 55, 12, 17,
  72, 62, 10,  6, 20, 19, 42, 46, 24, 78,
  42
]
non_adjacent_sum(nums) # -> 1465
```
