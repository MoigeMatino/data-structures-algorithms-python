# leaf list

Write a function, `leaf_list`, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

## test_00:

```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

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

leaf_list(a) # -> [ 'd', 'e', 'f' ] 
```

## test_01:

```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
g = Node("g")
h = Node("h")

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

leaf_list(a) # -> [ 'd', 'g', 'h' ]
```

## test_02:

```python
a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

leaf_list(a) # -> [ 20, 1, 3, 54 ]
```

## test_03:

```python
x = Node('x')

#      x

leaf_list(x) # -> [ 'x' ]
```

## test_04:

```python
leaf_list(None) # -> [ ]
```
