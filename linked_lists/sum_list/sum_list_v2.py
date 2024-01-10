def sum_list(head):
    if head is None:
        return 0
    return head.val + sum_list(head.next)

"""
n: number of nodes in linked list
Time: O(n)
Space: O(n); this is because of the call stack utilised by recursive algorithms
to manage function calls. Every time the recursive function is called a new stack
frame is added to the call stack, storing with it information about the function 
call, local variables and return addresses.
"""
