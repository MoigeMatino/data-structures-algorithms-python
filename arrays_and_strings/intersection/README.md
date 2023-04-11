# intersection

Write a function, `intersection`, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
## test_00:

`intersection([4,2,1,6], [3,6,9,2,10]) # -> [2,6]`

## test_01:

`intersection([2,4,6], [4,2]) # -> [2,4]`

## test_02:

`intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]`

## test_03:

`intersection([0,1,2], [10,11]) # -> []`

## test_04:

`a = [ i for i in range(0, 50000) ]`

`b = [ i for i in range(0, 50000) ]`

`intersection(a, b) # -> [0,1,2,3,..., 49999]`
