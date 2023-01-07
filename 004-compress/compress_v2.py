def compress(s):

    s += '!'
    result = []
    i = 0
    j = 0
    while j < len(s):
        if s[i] == s[j]:
            j += 1  
        else:
            num = j - i
            if num == 1:
                result.append(s[i])
            else:
                result.append(str(num)) 
                result.append(s[i])
            i = j
        
    return ''.join(result)

"""
================================================================================
Notes:
================================================================================
Strategy: Two pointers technique

Time complexity: O(n)
Space complexity: O(n)

The time complexity of this algorithm is linear time because we run n iterations. 
To note is that appending an item to the end of a list is a constant time operation.

To note: Adding the '!' token alllows us to access the last set of characters that are similar.
"""
