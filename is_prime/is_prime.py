from math import sqrt, floor

def is_prime(n):
  if n<2:
    return False
  # *Best explanation for using sqrt: https://stackoverflow.com/a/54544012/14753649
  for divisor in range(2,floor(sqrt(n)) +1):
    if n%divisor==0:
      return False

  return True

# TODO: Add time and space complexity