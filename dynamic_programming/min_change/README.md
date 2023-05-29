# min change

Write a function `min_change` that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.

```python
min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible
```

```python
min_change(13, [1, 9, 5, 14, 30]) # -> 5
```

```python
min_change(23, [2, 5, 7]) # -> 4
```

```python
min_change(102, [1, 5, 10, 25]) # -> 6
```

```python
min_change(200, [1, 5, 10, 25]) # -> 8
```

```python
min_change(2017, [4, 2, 10]) # -> -1
```

```python
min_change(271, [10, 8, 265, 24]) # -> -1
```

```python
min_change(0, [4, 2, 10]) # -> 0
```

```python
min_change(0, []) # -> 0
```
