# linked list values

Write a function, `linked_list_values`, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.

## test_00

```
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

a -> b -> c -> d

linked_list_values(a) # -> [ 'a', 'b', 'c', 'd' ]
```

## test_01

```
x = Node("x")
y = Node("y")

x.next = y

# x -> y

linked_list_values(x) # -> [ 'x', 'y' ]
```

## test_02

```
q = Node("q")

# q

linked_list_values(q) # -> [ 'q' ]
```

## test_03

```
linked_list_values(None) # -> [ ]
```
