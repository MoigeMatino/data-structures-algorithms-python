class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def traverse(head):
    nodes=[]
    current = head
    while current is not None:
        nodes.append(current)
        current = current.next

    return nodes
