# linked list find

Write a function, `linked_list_find`, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.
## test_00:
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "c") # True
```

## test_01:
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "d") # True
```

## test_02:
```python
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "q") # False
```

## test_03:
```python
node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

linked_list_find(node1, "jason") # True
```

## test_04:
```python
node1 = Node(42)

# 42

linked_list_find(node1, 42) # True
```

## test_05:
```python
node1 = Node(42)

# 42

linked_list_find(node1, 100) # False
```
