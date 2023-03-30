def get_node_value(head, index):
    counter = 0
    current = head
    while current is not None:
        if counter == index:
            return current.val
        current = current.next
        counter += 1
        
    return None

"""
Iterative approach
======================
n: number of nodes
Time: O(n)
Space: O(1)
"""