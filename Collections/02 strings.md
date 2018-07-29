# Strings 

## General

- homogeneous immutable sequence of unicode characters
- while the `+` operator can be used to concat strings, we should be using the `join()` method 
    - as it is way more efficient & the + way will lead to a big amount of temporates and thus
    - imlications for mem usage and other resources
- `.partition(seperator)` divides a string into 3 parts & returns a tuple `('prefix', 'seperator', 'suffix')`
    - often this is used in conjunction with tuple unpacking so seperate two values:
```python
origin, _, destination = "Seattle-Boston".partition('-')
```
- Here we'll have `origin = "Seattle"` & `destination = "Boston"`
- because it is widely adopted, not using the `_` variable won't throw an error / lint warning

## Formatting

- `.format(args)` can be used to insert values into strings, it will replace fields delimited by `{}`
    - Integer field names will be matched with positional arguments in format
    - if we use all values only once and in the order we are passing them to `format` we can ommit putting values
        - into our `.format` method
- it is also possible to access values through keys or indices w/ `[]` notation in the replacement fields! ex:
```python 
pos = (65.2, 23.1, 82.2)
'Galactic position x={pos[0]} y={pos[1]} z={pos[2]}'.format(pos=pos)
```
- will output ''Galactic position 65.2 23.1 82.2'
- we can even feed whole modules to `format` -> because as we know, `modules are objects` like everything else is
```python
import math
"Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math)
```
- in this case the `:.3f` is used to limit the decimals of our constants, this is part of the replacement field "mini language"