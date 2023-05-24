def compress(s):
    s += '@'
    result=''
    i=0
    j=0
    while j<len(s):
        if s[i] == s[j]:
            j+=1
        else:
            num=j-i
            if num==1:
                result+=s[i]
            else:
                result += str(num) + s[i]
            i=j

    return result

print(compress('ccaaatsss'))

"""
======================================================================================
Notes:
======================================================================================
Strategy: Two pointers technique

Time complexity: O(n^2)
Space complexity: O(n)

This is a less efficient solution:
Strings in python are immutable therefore concatenating strings
involves creating a copy of the string to new memory then making the addition.
This operation has linear time complexity. 
This time complexity of this algorithm is quadratic because we're running n iterations 
with a nested linear time from the concatenation operations on the strings.

Also, adding the '@' token is a neat trick!
"""
