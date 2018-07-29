# Lists

#### General

- heterogeneous mutable sequences
- index based access, zero & positive integers for `indexing from the front`
- negative -1 to -len() for indexing `back to front`
- Lists, like str & tuples also support the `repetition` operation (still only shallow copies)

- `index(arg)` returns the int index of the first occurence of arg or a ValueError if not found 
- `count(arg)` returns number of matching elements 
- `in` and `not in` operators only test for membership and return a bool

#### Slicing:

- slicing extracts part of a list using the `[start:stop]` syntax - start included, stop excluded
    - when slicing we can also use negative indices
    - if we want to slice including the end of the list, simply leave stop empy like `[1:]`
        - same goes for the start index
    - *important for creating actual copies of lists using `[:]`*
        - for this we can also use more readable methods like `copy()` or
        - a call to this list constructor `list(list)`
        - **the use of the list constructor is preferred, as it has the upside of working w/ all iterables**
        - all of these methods perform a shallow copy & only copy the references to the included objects!
            - this means that the new list is a different object than the copied list, however the included
                elements are still only references. *If these referenced objects change, our new list will*
                *change aswell!*
    - Screenshot of what this means: https://gyazo.com/ed663540e00c73aa65772ff3a16a7471

#### Removing + Inserting Elements

- removing elements works via the `del list[index]` syntax or by removing by value
    using `list.remove(value)` (raises a VE if not present)
        - `list.remove(value)` is the equivalent of `del list[list.index(value)]`, so not great.

- insert items using the `insert(index, value)` method

#### Concatenating Lists

- simply **concat** 2 lists using the `+` operator, this creates a new list, leaving the old ones intact
- using the `+=` operator changes the assignee (same as `extend()`)
```python
m = [2, 1, 3]
n = [4, 7, 11]
k = m + n  # leaves m & n intact!
# While for in place extension we use += or `extend()`
k += [7, 3, 88]
# k == [2, 1, 3, 4, 7, 11, 7, 3, 88]
```
- **All of these methods work w/ iterables on the right hand side, not only lists**

#### Reversing + Sorting Lists

- reverse by `reverse()`
- sort by `sort(reverse, key)`
    - sort, by default in ascending order can be reversed by setting reverse to True
    - `key` is used to sort by property of the element within the list
- **Simple example for the key arg that will sort these strings by lenth in ascending order:
```python
new_list = ['Bla', 'muuuh', 'KAKAKAKA', 'I']
new_list.sort(key=len)
```
- **`sorted`** is used if we do not want to mutate our original list, it returns a sorted shallow copy
- **`reversed`** reverses any iterable series & returns a reverse iterator -> have to use list() constructor to 
    turn it back into a list