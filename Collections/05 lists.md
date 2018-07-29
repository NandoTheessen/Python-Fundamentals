# Lists

- heterogeneous mutable sequences
- index based access, zero & positive integers for `indexing from the front`
- negative -1 to -len() for indexing `back to front`
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