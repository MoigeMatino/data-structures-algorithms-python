class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head):
    nodes=[]
    current = head
    while current:
        nodes.append(current.val)
        current = current.next

    return nodes
