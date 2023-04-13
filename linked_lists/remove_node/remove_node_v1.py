class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_node(head, target_val):
    prev = None
    current = head

    if head.val == target_val:
        return head.next
    
    while current is not None:
        if current.val == target_val:
            prev.next = current.next
            break
        
        prev = current
        current = current.next
    
    return head


"""
iterative approach
n - number of nodes
Time: O(n)
Space: O(1)

"""