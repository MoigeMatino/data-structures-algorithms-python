def max_value(nums):
  maximum = float('-inf')#to cater to negative integers
  for x in nums:
    if x>maximum:
      maximum=x
      
  return maximum


# TODO: Add time and space complexity
