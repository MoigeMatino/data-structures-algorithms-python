class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def node_values(head):
    nodes=[]
    traverse(head, nodes)
    return nodes


def traverse(head, nodes):
    if head == None:
        return
    
    nodes.append(head.val)
    traverse(head.next)

    

