class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(values, index=0):
    if index == len(values):
        return None
    
    head = Node(values[index])
    head.next = create_linked_list(values, index+1)
    return head