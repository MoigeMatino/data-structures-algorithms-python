# prereqs possible

Write a function, `prereqs_possible`, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.

## test_00

```python
numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
]
prereqs_possible(numCourses, prereqs) # -> True
```
## test_01

```python

numCourses = 6
prereqs = [
  (0, 1),
  (2, 3),
  (0, 2),
  (1, 3),
  (4, 5),
  (3, 0),
]
prereqs_possible(numCourses, prereqs) # -> False
```
## test_02

```python

numCourses = 5
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
]
prereqs_possible(numCourses, prereqs) # -> True
```
## test_03

```python

numCourses = 6
prereqs = [
  (2, 4),
  (1, 0),
  (0, 2),
  (0, 4),
  (5, 3),
  (3, 5),
]
prereqs_possible(numCourses, prereqs) # -> False
```
## test_04

```python

numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> True
```

## test_05

```python

numCourses = 8
prereqs = [
  (1, 0),
  (0, 6),
  (2, 0),
  (0, 5),
  (3, 7),
  (7, 4),
  (4, 3),
]
prereqs_possible(numCourses, prereqs) # -> False
```

## test_06

```python

numCourses = 42
prereqs = [(6, 36)]
prereqs_possible(numCourses, prereqs) # -> True#
```
