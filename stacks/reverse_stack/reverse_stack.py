def reverse_stack(stack):
    """
    Reverses the elements of a stack using recursion (in-place modification).

    Args:
        stack: A stack-like data structure (list in this case) to be reversed.

    Returns:
        stack that is reversed (modified in-place).
    """
    def insert_at_bottom(stack, item):
        """
        Helper function to insert an element at the bottom of the stack recursively.

        Args:
            stack: The stack to insert the element into.
            item: The element to be inserted.
        """
        if not stack: # Checks if the stack is empty. 
            stack.append(item) # If empty, appends the item to the bottom (directly).
            return # Returns from the function (no further recursion)-> passes control back to the caller.
        temp = stack.pop() # Pops the top element from the stack and stores it temporarily.
        insert_at_bottom(stack, item) # Appends the item to the bottom of the stack by making a recursive call with the remaining items.
        stack.append(temp) # Appends the temporarily popped element back onto the stack

    if not stack: # Base case: If the stack is empty, returns without doing anything
        return [] 
    item = stack.pop() # Pops the top element from the stack
    reverse_stack(stack) # Recursively calls reverse_stack on the remaining stack (excluding the popped element).
    insert_at_bottom(stack, item) # Calls the helper function to insert the popped element at the bottom of the reversed stack.
    return stack

"""
Time Complexity: O(n)
The function makes recursive calls proportional to the number of elements (n) in the stack.

Space Complexity: O(n) 
The recursive calls utilize the call stack for temporary storage, and in the worst-case scenario 
with a skewed stack, the call stack depth can be proportional to the stack height.

Further Notes:
The reverse_stack function works recursively. It pops elements from the stack and makes recursive calls 
on the remaining elements. A helper function insert_to_bottom is used to insert the popped elements at 
the bottom of the reversed sub-stack during recursion. This process iteratively builds the reversed stack.

"""


        
