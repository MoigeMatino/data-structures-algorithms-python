# knightly number

A knight is on a chess board. Can you figure out the total number of ways the knight can move to a target position in exactly m moves? On a single move, the knight can move in an "L" shape; two spaces in any direction, then one space in a perpendicular direction. This means that on a single move, a knight has eight possible positions it can move to.

Write a function, knightlyNumber, that takes in 6 arguments:

n, m, kr, kc, pr, pc

    n = the length of the chess board
    m = the number of moves that must be used
    kr = the starting row of the knight
    kc = the starting column of the knight
    pr = the target row
    pc = the target column

The function should return the number of different ways the knight can move to the target in exactly m moves. The knight can revisit positions of the board if needed. The knight cannot move out-of-bounds of the board. You can assume that rows and columns are 0-indexed. This means that if n = 8, there are 8 rows and 8 columns numbered 0 to 7.

```python
knightly_number(8, 2, 4, 4, 5, 5) # -> 2
```

```python
knightly_number(8, 2, 7, 1, 7, 1) # -> 3
```

```python
knightly_number(8, 2, 5, 4, 5, 4) # -> 8
```

```python
knightly_number(8, 3, 5, 2, 4, 4) # -> 21
```

```python
knightly_number(20, 6, 18, 7, 10, 15) # -> 60
```

```python
knightly_number(20, 12, 8, 3, 9, 14) # -> 98410127
```

```python
knightly_number(8, 2, 0, 0, 1, 1) # -> 0
```
