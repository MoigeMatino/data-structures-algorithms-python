# longest path

Write a function, `longest_path`, that takes in an adjacency list for a **directed acyclic graph**. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.

## test 00

```python

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2
```

## test 01

```python

graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': [],
  'q': ['r'],
  'r': ['s', 'u', 't'],
  's': ['t'],
  't': ['u'],
  'u': []
}

longest_path(graph) # -> 4
```

## test 02

```python

graph = {
  'h': ['i', 'j', 'k'],
  'g': ['h'],
  'i': [],
  'j': [],
  'k': [],
  'x': ['y'],
  'y': []
}

longest_path(graph) # -> 2
```

## test 03

```python

graph = {
  'a': ['b'],
  'b': ['c'],
  'c': [],
  'e': ['f'],
  'f': ['g'],
  'g': ['h'],
  'h': []
}

longest_path(graph) # -> 3
```
