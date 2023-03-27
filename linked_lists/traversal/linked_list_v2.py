class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

nodes=[]
def traverse(head):
    current = head
    if head == None:
        return []
    
    nodes.append(current.val)
    traverse(current.next)

    return nodes

