# paired parentheses

Write a function,  `paired_parentheses`, that takes in a string as an argument. The function should return a boolean indicating whether or not the string has well-formed parentheses.

You may assume the string contains **only** alphabetic characters, '(', or ')'.

## test_00

```python
paired_parentheses("(david)((abby))") # -> True
```

## test_01

```python
paired_parentheses("()rose(jeff") # -> False
```

## test_02

```python
paired_parentheses(")(") # -> False
```

## test_03

```python
paired_parentheses("()") # -> True
```

## test_04

```python
paired_parentheses("(((potato())))") # -> True
```

## test_05

```python
paired_parentheses("(())(water)()") # -> True
```

## test_06

```python
paired_parentheses("(())(water()()") # -> False
```

## test_07

```python
paired_parentheses("") # -> True
```

## test_08

```python
paired_parentheses("))()") # False
```
