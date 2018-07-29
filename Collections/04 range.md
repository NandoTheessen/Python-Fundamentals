# Range

- arithmetic progression of ints
- called by `range()` constructor
    - `range(int)` gives us a sequence from `0 to int - 1`
- we can also pass a `step argument`, so we have to supply all 3 arguments in order to use it!

- **It would be considered unpythonic to actually use range in a for loop!**
    - it is much better to simply iterate over an object
    - **If a counter is needed, use the `enumerate(iterable)` method**
        - this will return a tuple with `(counter, value)`
        - often used with `tuple unpacking`!
        example where `i` stands for the index & `v` stands for the value:
        ```python
        for i, v in enumarate(t):
            print("i ={}, v = {}".format(i, v))
        ```