# reverse list

Write a function, `reverse_list`, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.

## test_00:

```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f

reverse_list(a) # f -> e -> d -> c -> b -> a
```

## test_01:

```python
x = Node("x")
y = Node("y")

x.next = y

# x -> y

reverse_list(x) # y -> x
```

## test_02:

```python
p = Node("p")

# p

reverse_list(p) # p
```
