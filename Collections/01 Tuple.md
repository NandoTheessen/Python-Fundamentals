# Tuple

## General

- iterable
- immutable sequence of elements
- elements can be `accessed via bracket notation` [index]
- can be `concatenated` using the + operator
- can be `multiplied` by an integer -> (1, 2) * 2 = (1, 2, 1, 2)

## Creation 
- when creating 1 element tuples, include a trailing comma. 
    - otherwise this will be seen as integer
    - however an `empty` tuple can be declared w/ just `()`

- if we'd like to `cast to a tuple` like a list or str:
    - use the `tuple()` constructor

- as with other collection types, `in` & `not in` operators can be used w/ tuples

## Tuple Unpacking

- very similar to destructuring in JS
- example: 
- **here a = 23, b = 45, c = 88**
```python
a, b, c = (23, 45, 88)
```

