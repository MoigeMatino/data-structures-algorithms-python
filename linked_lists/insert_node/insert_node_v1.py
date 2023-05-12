class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, value, index):
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node

    count = 0
    current = head
    while current is not None:
        if count == index-1:
            temp = current.next
            current.next = Node(value)
            current.next.next = temp
        count += 1
        current = current.next
    
    return head

"""
Iterative approach
n - number of nodes
Time: O(n)
Space: O(1)
"""
