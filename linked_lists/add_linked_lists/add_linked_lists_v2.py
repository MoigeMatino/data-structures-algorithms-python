class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

def add_lists(head_1, head_2, carry = 0):
    if head_1 is None and head_2 is None and carry == 0:
        return None
    
    val_1 = 0 if head_1 is None else head_1.val
    val_2 = 0 if head_2 is None else head_2.val  
    sum = val_1 + val_2 + carry
    next_carry = 1 if sum > 9 else 0
    digit = sum % 10
    
    result = Node(digit)
    
    next_1 = None if head_1 is None else head_1.next
    next_2 = None if head_2 is None else head_2.next
    
    result.next = add_lists(next_1, next_2, next_carry)
    return result

"""

n = length of list 1
m = length of list 2
Time: O(max(n, m))
Space: O(max(n, m))

"""