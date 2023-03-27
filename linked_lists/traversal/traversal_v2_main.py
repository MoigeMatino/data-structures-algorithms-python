class Node:
    def __init__(self, val):
        self.val = val
        self.next = next

def node_values(head):
    nodes_list=[]
    traverse(head, nodes_list)
    return nodes_list


def traverse(head, nodes):
    if head == None:
        return
    
    nodes.append(head.val)
    traverse(head.next, nodes)

