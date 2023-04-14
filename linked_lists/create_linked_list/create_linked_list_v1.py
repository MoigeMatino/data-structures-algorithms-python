class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values):
    dummy_head = Node(None)
    tail = dummy_head
    for value in values:
        tail.next = Node(value)
        tail = tail.next
    
    return dummy_head.next