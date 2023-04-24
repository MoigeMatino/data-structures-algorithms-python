# breadth first values

Write a function, `breadth_first_values`, that takes in the root of a binary tree. The function should return a list containing all values of the tree in breadth-first order.

## test_00:

```python
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'd', 'e', 'f']
```

## test_01:

```python
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g
f.right = h

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

breadth_first_values(a) 
#   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

## test_02:

```python
a = Node('a')

#      a

breadth_first_values(a) 
#    -> ['a']
```

## test_03:

```python
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
x = Node('x')

a.right = b
b.left = c
c.left = x
c.right = d
d.right = e

#      a
#       \
#        b
#       /
#      c
#    /  \
#   x    d
#         \
#          e

breadth_first_values(a) 
#    -> ['a', 'b', 'c', 'x', 'd', 'e']
```

## test_04:

```python
breadth_first_values(None) 
#    -> []
```
