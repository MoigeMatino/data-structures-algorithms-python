class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def insert_node(head, value, index, count=0):
    if index == 0:
        new_head = Node(value)
        new_head.next=head
        return new_head
    
    if count == index-1:
        temp = head.next
        head.next = Node(value)
        head.next.next = temp
        return
    
    insert_node(head.next, value, index, count+1)
    return head
    
"""
Recursive approach
n - number of nodes
Time: O(n)
Space: O(n)
"""