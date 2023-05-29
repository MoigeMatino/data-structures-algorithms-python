# sum possible

Write a function `sum_possible` that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.

```python
sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
```

```python
sum_possible(15, [6, 2, 10, 19]) # -> False
```

```python
sum_possible(13, [6, 2, 1]) # -> True
```

```python
sum_possible(103, [6, 20, 1]) # -> True
```

```python
sum_possible(12, []) # -> False
```

```python
sum_possible(12, [12]) # -> True
```

```python
sum_possible(0, []) # -> True
```

```python
sum_possible(271, [10, 8, 265, 24]) # -> False
```

```python
sum_possible(2017, [4, 2, 10]) # -> False
```

```python
sum_possible(13, [3, 5]) # -> true
```
