# Summary

## Tuples:
- immutable sequence types
    - literal syntax: optional parens around a comma seperated list
    - Single element tuples must use a trailing comma
    - `Tuple unpacking` is very useful! (for `idiomatic swaps` as well as return values)

## Strings
- immutable sequence types of Unicode characters
    - String concatenation is most efficiently performed w/ `join()` on an empty seperator
    - the `partition()` method is a useful and elegant str parsing tool 
    - the `format()` method provides a powerful way of injecting values into strings

## Ranges
- represent integer seq. w/ regular intervals
    - arithmetic progressions
    - the `enumerate()` function is often a superior alternative to range!!

## Lists
- heterogeneous mutable seq types
    - netive indices work backwards from the end
    - Slicing allows us to copy all or part of a list 
    - full slice (`[:]`) is a common idiom for copying lists, although the constructor & / the `copy()`
        method give better readability
    - Copys are shallow
    - List repetition is shallow (`[0] * 50` for example)

## Dictionaries
- map immutable keys to mutable values
    - iteration and membership testing is done in respect to keys only
    - order is arbitrary
    - The `keys()`, `values()` and `items()` methods give more convenient iteration opportunities
    - prettier printing should be used to give a better representation of dicts 

## Sets
- store unordered collections of unique elements
    - Support powerful and expressive set algebra operations and predicates

## Protocols
- such as iterable, sequence and container characterise the collections