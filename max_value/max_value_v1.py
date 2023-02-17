def max_value(nums):
  maximum = float('-inf')#to cater to negative integers
  for x in nums:
    if x>maximum:
      max_value=x
      
  return max_value

# TODO: Add time and space complexity