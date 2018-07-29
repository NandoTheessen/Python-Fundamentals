# Protocols

- to be able to implement a 'protocol' a type *must* support a set of operations
    - protocols must not be written in the source code, it is enough for our
        object to support the necessary operations

- For example:
    - `Container`: must support `membership testing` 
    - `Sized`: must support the `len()` method
    `Iterable`: must be able to create an iterable using the `iter()` constructor
        - basically, has to be able to be looped over
    - `Sequence`: Access elements by index `[]`, find items by value `.index(value)`
        count items by `.count(item)` & produce a reversed sequence using `reversed(seq)`