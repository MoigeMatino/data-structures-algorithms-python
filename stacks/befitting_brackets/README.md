# befitting brackets

Write a function, `befitting_brackets`, that takes in a string as an argument. The function should return a boolean indicating whether or not the string contains correctly matched brackets.

You may assume the string contains only characters: ( ) [ ] { }

## test_00

```python
befitting_brackets('(){}[](())') # -> True
```

## test_01

```python
befitting_brackets('({[]})') # -> True
```

## test_02

```python
befitting_brackets('[][}') # -> False
```

## test_03

```python
befitting_brackets('{[]}({}') # -> False
```

## test_04

```python
befitting_brackets('[]{}(}[]') # -> False
```

## test_05

```python
befitting_brackets('[]{}()[]') # -> True
```

## test_06

```python
befitting_brackets(']{}') # -> False
```

## test_07

```python
befitting_brackets('') # -> True
```

## test_08

```python
befitting_brackets("{[(}])") # -> False
```
