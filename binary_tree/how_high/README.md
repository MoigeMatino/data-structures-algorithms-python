# how high

Write a function, `how_high`, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.

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

how_high(a) # -> 2
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

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /
#   g

how_high(a) # -> 3
```

## test_02:

```python
a = Node('a')
c = Node('c')

a.right = c

#      a
#       \
#        c

how_high(a) # -> 1
```

## test_03:

```python
a = Node('a')

#      a

how_high(a) # -> 0
```

## test_04:

```python
how_high(None) # -> -1
```
