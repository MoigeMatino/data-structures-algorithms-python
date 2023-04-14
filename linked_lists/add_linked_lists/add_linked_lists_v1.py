class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def add_lists(head_1, head_2):
    dummy_head = Node(None)
    tail = dummy_head
    
    carry = 0
    current_1 = head_1
    current_2 = head_2
    while current_1 is not None or current_2 is not None or carry == 1:
        val_1 = 0 if current_1 is None else current_1.val
        val_2 = 0 if current_2 is None else current_2.val
        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10
        
        tail.next = Node(digit)
        tail = tail.next
        
        if current_1 is not None:
            current_1 = current_1.next
        
        if current_2 is not None:
            current_2 = current_2.next
        
    return dummy_head.next