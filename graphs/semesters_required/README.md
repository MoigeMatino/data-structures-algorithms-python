# semesters required

Write a function, `semesters_required`, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.

## test_00

```python
num_courses = 6
prereqs = [
  (1, 2),
  (2, 4),
  (3, 5),
  (0, 5),
]
semesters_required(num_courses, prereqs) # -> 3
```

## test_01

```python
num_courses = 7
prereqs = [
  (4, 3),
  (3, 2),
  (2, 1),
  (1, 0),
  (5, 2),
  (5, 6),
]
semesters_required(num_courses, prereqs) # -> 5
```

## test_02

```python
num_courses = 5
prereqs = [
  (1, 0),
  (3, 4),
  (1, 2),
  (3, 2),
]
semesters_required(num_courses, prereqs) # -> 2
```

## test_03

```python
num_courses = 12
prereqs = []
semesters_required(num_courses, prereqs) # -> 1
```

## test_04

```python
num_courses = 3
prereqs = [
  (0, 2),
  (0, 1),
  (1, 2),
]
semesters_required(num_courses, prereqs) # -> 3
```

## test_05

```python
num_courses = 6
prereqs = [
  (3, 4),
  (3, 0),
  (3, 1),
  (3, 2),
  (3, 5),
]
semesters_required(num_courses, prereqs) # -> 2
```
