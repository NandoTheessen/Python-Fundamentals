# Sets

## General
- *unordered* collection of *unique* and *immutable* objects
- as membership operations are fundamental for sets `in` & `not in` operators can be used
- delimited by `{}`, but contrary to dicts only possess keys seperated by a `,`
- since using empty `{}` creates a new dict, creating a set works by using 
    the set constructor `set()`
    - the constructor can again take any `iterable` and will remove all duplicates

## Manipulating Sets
- to add an element use `set.add(element)`
    - adding an already existing element has no effect
- to add multiple elements we can use the `set.update(iterable)` method

- Removing from sets is being done in two ways: 
    - `set.remove(object)` which raises a key error if object isn't present
    - `k.discard(object)` does the same but raises no errors if object is not present 

- Creating shallow copies works the same way as with all other collections, using either `copy()`
    or the constructor `set()`

## Set Algebra operations
- **`set.union(set)`** method:
    - returns a set which contains all values that are either in one of the sets or in both
- **`set.intersection(set)`** method:
    - returns a set which contains all values that are present in **both** sets
- **`set.difference(set)`** method:
    - returns a set which contains all values that are **only** in the first set
- **`set.symmetric_difference(set)`** method:
    - returns a set which are in **either or** the second set but *not* both

- **`set.issubset(set)`** method: 
    - checks if this set is contained in the set passed in as arg
- **`set.issuperset(set)`** method:
    - checks if the passed in set is a subset of this set
- **`set.isdisjoint(set)`** method:
    - checks if both sets don't have any values in common